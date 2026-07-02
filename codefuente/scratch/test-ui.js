const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    console.log("Navigating to login...");
    await page.goto('http://localhost:3000/login');
    
    await page.fill('input[name="email"]', 'procurer@example.com');
    await page.fill('input[name="password"]', '123456');
    await page.click('button[type="submit"]');
    
    console.log("Waiting for dashboard...");
    await page.waitForURL('http://localhost:3000/');
    
    console.log("Navigating to suspicions...");
    await page.goto('http://localhost:3000/suspicions');
    await page.waitForSelector('table');
    
    console.log("Clicking first suspicion...");
    // The link might be an anchor tag or button. Let's just go to the first suspicion directly if we can, or click the first row.
    // Let's find an anchor tag that goes to /suspicions/
    const firstLink = await page.$('a[href^="/suspicions/"]');
    if (!firstLink) {
      console.log("No suspicion found!");
      process.exit(1);
    }
    const href = await firstLink.getAttribute('href');
    console.log(`Going to ${href}...`);
    await page.goto(`http://localhost:3000${href}`);
    
    console.log("Clicking 'Agregar criterio de inclusión'...");
    // Find button containing text
    await page.click('button:has-text("Agregar criterio de inclusión")');
    
    console.log("Waiting for modal...");
    await page.waitForSelector('text=Agregar criterio de inclusión', { state: 'visible' });
    
    console.log("Uploading file...");
    // Material UI Dropzone uses an input type=file hidden inside
    // FormDropzoneArea for VIH uses name="vih" ? No, the DropzoneArea doesn't set name on input.
    // We can just set the file on the first input[type="file"]
    const fileInput = await page.$('input[type="file"]');
    await fileInput.setInputFiles(path.resolve(__dirname, 'test1.pdf'));
    
    console.log("Checking checkboxes for hasCancer and hasSepsis (required false)...");
    // The schema says hasCancer and hasSepsis are required booleans.
    // We can just click the "No" checkboxes for cancer and sepsis to make them false, or whatever is required.
    // Actually, looking at the dialog, it might just need clicking.
    // Wait, let's just try to submit and see if validation fails.
    console.log("Submitting form...");
    await page.click('button:has-text("Guardar")');
    
    // Wait for success snackbar or dialog to close
    await page.waitForTimeout(3000);
    
    console.log("Checking if modal closed...");
    const isVisible = await page.isVisible('text=Completa el formulario con los datos.');
    if (isVisible) {
      console.log("Modal is still open, meaning there was an error or validation issue.");
      const errorHTML = await page.innerHTML('.MuiDialog-paper');
      console.log("Modal HTML:");
      console.log(errorHTML);
      process.exit(1);
    }
    
    console.log("SUCCESS! Test passed.");
  } catch (err) {
    console.error("Test failed:", err);
  } finally {
    await browser.close();
  }
})();

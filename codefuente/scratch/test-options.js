async function testCors() {
  const url = "https://trasplan-files-dev.s3.us-east-2.amazonaws.com/uploads/test.pdf?x-id=PutObject";

  try {
    const res = await fetch(url, {
      method: "OPTIONS",
      headers: {
        "Origin": "http://localhost:3000",
        "Access-Control-Request-Method": "PUT",
        "Access-Control-Request-Headers": "authorization,content-type,x-amz-content-sha256,x-amz-date,x-amz-security-token,x-amz-user-agent"
      }
    });

    console.log("Status:", res.status);
    console.log("Headers:");
    res.headers.forEach((value, name) => {
      console.log(`  ${name}: ${value}`);
    });
    
    const text = await res.text();
    console.log("Body:", text);
  } catch (e) {
    console.error("Error:", e);
  }
}

testCors();

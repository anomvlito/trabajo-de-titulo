const { S3Client, PutObjectCommand } = require("@aws-sdk/client-s3");

const fs = require('fs');

async function testFlow() {
  console.log("1. Authenticating as procurer...");
  const loginRes = await fetch('http://localhost:8080/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        mutation Login($email: String!, $password: String!) {
          login(email: $email, password: $password)
        }
      `,
      variables: { email: "procurer@example.com", password: "123456" }
    })
  });
  const loginData = await loginRes.json();
  const token = loginData.data?.login;
  if (!token) throw new Error("Login failed");

  console.log("2. Generating STS credentials...");
  const stsRes = await fetch('http://localhost:8080/graphql', {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
      query: `
        query {
          generateS3AccessCredentials {
            AccessKeyId
            SecretAccessKey
            SessionToken
          }
        }
      `
    })
  });
  const stsData = await stsRes.json();
  const creds = stsData.data?.generateS3AccessCredentials;
  if (!creds) throw new Error("STS failed");

  console.log("3. Uploading PDF to S3 using STS credentials...");
  const s3Client = new S3Client({
    region: "us-east-2",
    credentials: {
      accessKeyId: creds.AccessKeyId,
      secretAccessKey: creds.SecretAccessKey,
      sessionToken: creds.SessionToken,
    },
  });

  const pdfBuffer = fs.readFileSync('/home/fabian/src/codefuente/scratch/test1.pdf');
  const fileName = `uploads/test_vih_${Date.now()}.pdf`;
  
  await s3Client.send(
    new PutObjectCommand({
      Bucket: "trasplan-files-dev",
      Key: fileName,
      Body: pdfBuffer,
      ContentType: "application/pdf",
    })
  );
  
  const fileUrl = `https://trasplan-files-dev.s3.us-east-2.amazonaws.com/${fileName}`;
  console.log("Uploaded successfully:", fileUrl);

  console.log("4. Getting first active suspicion to attach criteria...");
  const susRes = await fetch('http://localhost:8080/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
    body: JSON.stringify({
      query: `
        query {
          getSuspicions {
            id
            status
          }
        }
      `
    })
  });
  const susData = await susRes.json();
  const suspicionId = susData.data.getSuspicions[0]?.id;
  if (!suspicionId) throw new Error("No suspicion found");

  console.log("5. Submitting Inclusion Criteria...");
  const incRes = await fetch('http://localhost:8080/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
    body: JSON.stringify({
      query: `
        mutation CreateInclusionCriteria($input: InclusionCriteriaInput!) {
          createInclusionCriteria(inclusionCriteriaInput: $input) {
            id
            vih
            hasSepsis
            hasCancer
          }
        }
      `,
      variables: {
        input: {
          values: {
            vih: fileUrl,
            vhb: "",
            vhc: "",
            hasSepsis: false,
            hasCancer: false,
            comments: "Test VIH PDF uploaded successfully via STS"
          },
          suspicionId: parseInt(suspicionId)
        }
      }
    })
  });
  
  const incData = await incRes.json();
  if (incData.errors) {
    console.error("GraphQL Error:", JSON.stringify(incData.errors, null, 2));
  } else {
    console.log("Inclusion Criteria created successfully!");
    console.log(JSON.stringify(incData.data, null, 2));
  }
}

testFlow().catch(console.error);

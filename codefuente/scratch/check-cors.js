const { S3Client, GetBucketCorsCommand } = require("@aws-sdk/client-s3");
const { STSClient, AssumeRoleCommand } = require("@aws-sdk/client-sts");

async function checkCORS() {
  require('dotenv').config({ path: '/home/fabian/src/codefuente/backend/.env' });
  
  const stsClient = new STSClient({
    region: "us-east-2",
    credentials: {
      accessKeyId: process.env.STS_IAM_ID,
      secretAccessKey: process.env.STS_IAM_SECRET,
    }
  });

  try {
    const assumeRole = await stsClient.send(new AssumeRoleCommand({
      RoleArn: process.env.STS_ROLE_ARN,
      RoleSessionName: "CheckCORS"
    }));

    const s3Client = new S3Client({
      region: "us-east-2",
      credentials: {
        accessKeyId: assumeRole.Credentials.AccessKeyId,
        secretAccessKey: assumeRole.Credentials.SecretAccessKey,
        sessionToken: assumeRole.Credentials.SessionToken,
      }
    });

    const res = await s3Client.send(
      new GetBucketCorsCommand({
        Bucket: "trasplan-files-dev"
      })
    );
    console.log("CORS Configuration:", JSON.stringify(res.CORSRules, null, 2));
  } catch (err) {
    console.error("Error getting CORS:", err);
  }
}

checkCORS();

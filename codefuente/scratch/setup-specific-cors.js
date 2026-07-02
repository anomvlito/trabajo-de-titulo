const { S3Client, PutBucketCorsCommand } = require("@aws-sdk/client-s3");
const { STSClient, AssumeRoleCommand } = require("@aws-sdk/client-sts");

async function setupSpecificCORS() {
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
      RoleSessionName: "SetupSpecificCORS"
    }));

    const s3Client = new S3Client({
      region: "us-east-2",
      credentials: {
        accessKeyId: assumeRole.Credentials.AccessKeyId,
        secretAccessKey: assumeRole.Credentials.SecretAccessKey,
        sessionToken: assumeRole.Credentials.SessionToken,
      }
    });

    console.log("Applying strict CORS to trasplan-files-dev...");
    await s3Client.send(
      new PutBucketCorsCommand({
        Bucket: "trasplan-files-dev",
        CORSConfiguration: {
          CORSRules: [
            {
              AllowedHeaders: ["*"], // S3 handles wildcard headers correctly
              AllowedMethods: ["PUT", "POST", "GET", "DELETE", "HEAD"],
              AllowedOrigins: [
                "http://localhost:3000",
                "https://localhost:3000",
                "http://127.0.0.1:3000",
                "https://trasplan2026.vercel.app"
              ],
              ExposeHeaders: ["ETag"],
              MaxAgeSeconds: 3000
            }
          ]
        }
      })
    );
    console.log("Strict CORS applied successfully!");
  } catch (err) {
    console.error("Error setting CORS:", err);
  }
}

setupSpecificCORS();

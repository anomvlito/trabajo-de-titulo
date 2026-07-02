const { S3Client, PutBucketCorsCommand } = require("@aws-sdk/client-s3");
const { STSClient, AssumeRoleCommand } = require("@aws-sdk/client-sts");

async function setupCORS() {
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
      RoleSessionName: "SetupCORS"
    }));

    const s3Client = new S3Client({
      region: "us-east-2",
      credentials: {
        accessKeyId: assumeRole.Credentials.AccessKeyId,
        secretAccessKey: assumeRole.Credentials.SecretAccessKey,
        sessionToken: assumeRole.Credentials.SessionToken,
      }
    });

    console.log("Applying CORS to trasplan-files-dev...");
    await s3Client.send(
      new PutBucketCorsCommand({
        Bucket: process.env.S3_BUCKET_NAME || "trasplan-files-dev",
        CORSConfiguration: {
          CORSRules: [
            {
              AllowedHeaders: ["*"],
              AllowedMethods: ["PUT", "POST", "GET", "DELETE", "HEAD"],
              AllowedOrigins: ["*"],
              ExposeHeaders: ["ETag"],
              MaxAgeSeconds: 3000
            }
          ]
        }
      })
    );
    console.log("CORS applied successfully!");
  } catch (err) {
    console.error("Error setting CORS:", err);
  }
}

setupCORS();

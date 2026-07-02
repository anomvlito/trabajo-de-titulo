const { S3Client, ListObjectsV2Command } = require("@aws-sdk/client-s3");
const { STSClient, AssumeRoleCommand } = require("@aws-sdk/client-sts");

async function listFiles() {
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
      RoleSessionName: "ListFiles"
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
      new ListObjectsV2Command({
        Bucket: "trasplan-files-dev",
        Prefix: "uploads/1783" // Get recent uploads
      })
    );
    console.log("Recent files:", res.Contents ? res.Contents.map(c => c.Key) : "No files found");
  } catch (err) {
    console.error("Error listing files:", err);
  }
}

listFiles();

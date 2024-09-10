require('dotenv').config();
const { BedrockEmbeddings } = require("@langchain/community/embeddings/bedrock");
const { Bedrock } = require("@langchain/community/llms/bedrock");


function getAzureOpenAIVariables() {
    const EMBEDDINGS = process.env.EMBEDDINGS_DEPLOYMENT_NAME;
    const AWS_ACCESS_KEY_ID = process.env.AWS_ACCESS_KEY_ID;
    const AWS_REGION = process.env.AWS_REGION;
    const AWS_SECRET_ACCESS_KEY = process.env.AWS_SECRET_ACCESS_KEY;
    const COMPLETIONS = process.env.COMPLETIONS_DEPLOYMENT_NAME;

    return { AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, EMBEDDINGS, COMPLETIONS };
}

// Class to get Bedrock LLMs
function GetBedrockLLMs () {
    const { AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, COMPLETIONS } = getAzureOpenAIVariables();
  const llms = new Bedrock({
      model: COMPLETIONS, // You can also use e.g. "anthropic.claude-v2"
      region: AWS_REGION,
      credentials: {
        accessKeyId: AWS_ACCESS_KEY_ID,
        secretAccessKey: AWS_SECRET_ACCESS_KEY,
      },
    });
    return llms;
}

// Class to get Bedrock Embeddings
function GetBedrockEmbeddings() {
    const { AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, EMBEDDINGS } = getAzureOpenAIVariables();
    const embeddings = new BedrockEmbeddings({
      region: AWS_REGION,
      credentials: {
        accessKeyId:AWS_ACCESS_KEY_ID,
        secretAccessKey: AWS_SECRET_ACCESS_KEY,
      },
      model: EMBEDDINGS,
    });

    return embeddings;
}

module.exports = { GetBedrockLLMs, GetBedrockEmbeddings };
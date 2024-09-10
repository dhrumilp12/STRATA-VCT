const { GetBedrockLLMs, GetBedrockEmbeddings } = require('../services/bedrock');
const { BufferMemory } = require("langchain/memory");
const { ConversationChain } = require("langchain/chains");

const bedrock= GetBedrockLLMs();
const embeddings = GetBedrockEmbeddings();      

// Set up the conversation chain with error handling
let conversation;
try {
  conversation = new ConversationChain({
    embeddings: embeddings,
    llm: bedrock,
    verbose: true,
    memory: new BufferMemory()
  });
} catch (error) {
  console.error("Failed to initialize the conversation chain:", error);
}

module.exports = { conversation };

       

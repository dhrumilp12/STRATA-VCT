const { GetBedrockLLMs, GetBedrockEmbeddings } = require('../services/bedrock');
const { BufferMemory } = require("langchain/memory");
const { ConversationChain } = require("langchain/chains");
const {PromptTemplate}= require("@langchain/core/prompts");

const bedrock= GetBedrockLLMs();
const embeddings = GetBedrockEmbeddings();

const customPrompt = PromptTemplate.fromTemplate( "you will use provided data sources to demonstrate effective information retrieval and analysis.\n\nCurrent conversation:\n\nHuman: ${input}")

// Set up the conversation chain with error handling
let conversation;
try {
  conversation = new ConversationChain({
    embeddings: embeddings,
    llm: bedrock,
    verbose: true,
    memory: new BufferMemory(),
    prompt: customPrompt // Pass the custom prompt here
  });
} catch (error) {
  console.error("Failed to initialize the conversation chain:", error);
}

module.exports = { conversation };

       

from services.bedrock import GetBedrockLLMs, GetBedrockEmbeddings
from langchain.memory import BufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

bedrock = GetBedrockLLMs()
embeddings = GetBedrockEmbeddings()

custom_prompt = PromptTemplate(
    template="you will use provided data sources to demonstrate effective information retrieval and analysis.\n\nCurrent conversation:\n\nHuman: {input}"
)

conversation = None
try:
    conversation = ConversationChain(
        embeddings=embeddings,
        llm=bedrock,
        verbose=True,
        memory=BufferMemory(),
        prompt=custom_prompt  
    )
except Exception as error:
    print(f"Failed to initialize the conversation chain: {error}")

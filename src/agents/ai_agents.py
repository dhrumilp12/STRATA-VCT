from src.services.bedrock import get_bedrock_llms, get_bedrock_embeddings
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

bedrock = get_bedrock_llms()
embeddings = get_bedrock_embeddings()

custom_prompt = PromptTemplate(
    template="you will use provided data sources to demonstrate effective information retrieval and analysis.\n\nCurrent conversation:\n\nHuman: {input}"
)

conversation = None
try:
    conversation = ConversationChain(
        llm=bedrock,
        verbose=True,
        memory=ConversationBufferMemory(),
        prompt=custom_prompt  
    )
except Exception as error:
    print(f"Failed to initialize the conversation chain: {error}")

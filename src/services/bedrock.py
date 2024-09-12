import os
from dotenv import load_dotenv
from langchain_aws import BedrockLLM, BedrockEmbeddings


load_dotenv()

def get_azure_openai_variables():
    return {
        "EMBEDDINGS": os.getenv("EMBEDDINGS_DEPLOYMENT_NAME"),
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
        "AWS_REGION": os.getenv("AWS_REGION"),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "COMPLETIONS": os.getenv("COMPLETIONS_DEPLOYMENT_NAME")
    }

def get_bedrock_llms():
    variables = get_azure_openai_variables()
    llms = BedrockLLM(
        model_id=variables["COMPLETIONS"],  
        region_name=variables["AWS_REGION"],
        
    )
    return llms

def get_bedrock_embeddings():
    variables = get_azure_openai_variables()
    embeddings = BedrockEmbeddings(
         region_name=variables["AWS_REGION"],
        model_id=variables["EMBEDDINGS"]
    )
    return embeddings
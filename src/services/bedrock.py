import os
from dotenv import load_dotenv
from langchain.embeddings import BedrockEmbeddings
from langchain.llms import Bedrock

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
    llms = Bedrock(
        model=variables["COMPLETIONS"],  
        region=variables["AWS_REGION"],
        credentials={
            "aws_access_key_id": variables["AWS_ACCESS_KEY_ID"],
            "aws_secret_access_key": variables["AWS_SECRET_ACCESS_KEY"],
        }
    )
    return llms

def get_bedrock_embeddings():
    variables = get_azure_openai_variables()
    embeddings = BedrockEmbeddings(
        region=variables["AWS_REGION"],
        credentials={
            "aws_access_key_id": variables["AWS_ACCESS_KEY_ID"],
            "aws_secret_access_key": variables["AWS_SECRET_ACCESS_KEY"],
        },
        model=variables["EMBEDDINGS"]
    )
    return embeddings
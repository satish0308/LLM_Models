import os
import dotenv
from langchain_community.llms import HuggingFaceEndpoint
sec_key=os.getenv("HUGGING_FACE_API_KEY")
os.environ["HUGGINGFACE_ACCESS_TOKEN"] =sec_key


model = "sentence-transformers/all-mpnet-base-v2"

#llm=HuggingFaceEndpoint(repo_id=model_name,max_length=128,temperature=0.7,token=sec_key)

from langchain.llms import OpenAI
import os
from api_keys import openAI_key

os.environ["OPENAI_API_KEY"] = openAI_key

llm = OpenAI(model_name="text-curie-001", temperature=1)

result = llm("Write a poem")

print(result)
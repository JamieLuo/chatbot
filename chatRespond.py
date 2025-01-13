import random
from initVectorDB import vectorDB
from gradio_client import Client
from promptConstruct import constructPrompt

DB=vectorDB()
client = Client("http://127.0.0.1:9997/qwen2.5-instruct/") #locally hosted llm endpoint 
#client = Client("http://host.docker.internal:9997/qwen2.5-instruct/") #code is a docker container
def llm_response(message, history):
    topK = DB.query(message)
    prompt = constructPrompt(topK, message)
    return client.predict(
		message=prompt,
		param_2=512,
		param_3=1,
		param_4=prompt,
		api_name="/chat"
    )   
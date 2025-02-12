import gradio as gr
from chatRespond import llm_response

gr.ChatInterface(
    fn=llm_response, 
    type="messages",
    title="ChatBot",
    description="Chat with your knowledge base",
    theme="soft"
).launch(server_name="0.0.0.0", server_port=8080)

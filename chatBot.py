import gradio as gr
from chatRespond import llm_response
gr.ChatInterface(
    fn=llm_response, 
    type="messages"
).launch()
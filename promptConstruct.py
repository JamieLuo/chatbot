prompt_template ="""Use the following pieces of context to answer the question at the end. 
If you don't know the answer, please think rationally and answer from your own knowledge base 

{context}

Question: {question}"""

def constructPrompt(found_docs,message):
    PROMPT = prompt_template.format(context=found_docs,question=message)
    return PROMPT
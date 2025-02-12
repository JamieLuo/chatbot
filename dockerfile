FROM python:3.10

RUN echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > /etc/pip.conf

RUN pip install --upgrade pip

RUN pip install requests

RUN pip install gradio
RUN pip install gradio_client
RUN pip install langchain

RUN pip install langchain-community
RUN pip install langchain-qdrant
RUN pip install qdrant-client
RUN pip install fastembed
RUN pip install langchain-openai
RUN pip install pypdf
RUN pip install sentence-transformers

WORKDIR /chatBot

ENV HF_ENDPOINT=https://hf-mirror.com

RUN huggingface-cli download BAAI/bge-base-en-v1.5 --cache-dir /chatBot/cache

RUN pip install langchain-huggingface

COPY . /chatBot

ENV PORT=8080

EXPOSE 8080

CMD ["python", "chatBot.py"]

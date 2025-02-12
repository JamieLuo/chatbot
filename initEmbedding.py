from langchain_huggingface import HuggingFaceEmbeddings


class bgeEmbedding:
    model = None

    def __init__(self):
        model_name = "/chatBot/cache/models--BAAI--bge-base-en-v1.5/snapshots/a5beb1e3e68b9ab74eb54cfd186867f64f240e1a"
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {"normalize_embeddings": True}
        self.model = HuggingFaceEmbeddings(
            model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
        )

    def getEmbed(self):
        return self.model
    
        
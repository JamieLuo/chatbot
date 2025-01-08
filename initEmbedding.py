from langchain_community.embeddings import HuggingFaceBgeEmbeddings


class bgeEmbedding:
    model = None

    def __init__(self):
        model_name = "BAAI/bge-base-en-v1.5"
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {"normalize_embeddings": True}
        self.model = HuggingFaceBgeEmbeddings(
            model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
        )

    def getEmbed(self):
        return self.model
    
        
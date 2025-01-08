import loader as fileloader
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import RetrievalMode
from initEmbedding import bgeEmbedding

class vectorDB:
    docs = None
    embedModel = None
    path = "c:/users/lc/documents/wellav"
    qdrant = None

    def __init__(self):
        self.loadKnowledgeBase()
        self.getEmbedding()
        self.qdrant = QdrantVectorStore.from_documents(
            self.docs,
            embedding=self.embedModel,
            location=":memory:",
            collection_name="my_documents",
            retrieval_mode=RetrievalMode.DENSE,
        )

    def loadKnowledgeBase(self):
        loader=fileloader.fileloader(self.path)
        loader.loadallfiles()
        self.docs = loader.getfiles()

    def getEmbedding(self):
        bge=bgeEmbedding()
        self.embedModel= bge.getEmbed()

    def query(self,message):
        return self.qdrant.similarity_search(message) #return list of documents

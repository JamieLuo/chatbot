from langchain_community.document_loaders import PyPDFLoader,TextLoader,MergedDataLoader
from langchain.document_loaders import DirectoryLoader


class fileloader:

    path:str = ""

    def __init__(self, path):
        self.path = path

    def loadallfiles(self):
        loader1 = DirectoryLoader(self.path, glob=["**/*.txt","**/*.doc","**/*.epub"],loader_cls=TextLoader)
        loader2 = DirectoryLoader(self.path, glob="**/*.pdf",loader_cls=PyPDFLoader)
        loader=MergedDataLoader([loader1,loader2])
        self.filelist=loader.load()

    def getfiles(self):
        return self.filelist
    
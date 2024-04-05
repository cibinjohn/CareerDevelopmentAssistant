from langchain.schema import Document
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from env.environment_variables import APPCONFIG
from log.cj_logger import cj_logger

class Retriever:

    def __init__(self):
        self.embeddings_name = "all-MiniLM-L6-v2"

        cj_logger.info("Loading embeddings")
        self.load_embeddings()
        cj_logger.info("Loaded embeddings...")

        cj_logger.info("Loading vector db")
        self.load_chroma_db()
        cj_logger.info("Loaded vector db...")

    def load_embeddings(self):
        self.embeddings = SentenceTransformerEmbeddings(model_name=self.embeddings_name)

    def load_chroma_db(self):
        self.db = Chroma(embedding_function=self.embeddings,
                         persist_directory=APPCONFIG.chroma_path)

    def retrieve_top_matching_documents(self, query, k=3):
        matching_docs = self.db.similarity_search(query)

        k = min(k, len(matching_docs))

        return [doc.page_content for doc in matching_docs[0:k]]

if __name__=="__main__":

    retriever = Retriever()
    query = "What is machine learning?"
    print(retriever.retrieve_top_matching_documents(query))

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from config.constants import CHROMA_DIR



class NaiveRag:
    def __init__(self,k=3  ):
        self.chroma_dir=CHROMA_DIR
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.k = k

        self.load_db()

    def load_db(self):
        print("Loading vector db")
        self.vectorstore = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=self.embeddings
        )
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": self.k})
        print("loaded vector db successfully...")

    def query(self,query):
        """
        Return top k chunks in the vector database similar to query
        :param query:
        :return: list of top k chunks
        """
        docs = self.retriever.invoke(query)
        if not docs:
            return "No relevant information found in the career knowledge base."

        results = []
        for i, doc in enumerate(docs, 1):
            # role = doc.metadata.get("role", "Unknown Role")
            results.append(f"{doc.page_content.strip()}")

        return results



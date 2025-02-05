import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="/home/makima/Documents/projects/cold-mail-generator/app/resources/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():

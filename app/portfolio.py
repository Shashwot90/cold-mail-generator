import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="/home/makima/Documents/projects/cold-mail-generator/app/resources/my_portfolio.csv"):
        self.file_path = file_path

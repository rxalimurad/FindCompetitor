import os
import pandas as pd 
import chromadb
from chromadb.utils import embedding_functions
from langchain.document_loaders import CSVLoader
import csv
import re

class FindCompetitors:
    def __init__(self):
        # Initializing chroma vector database 
        self.CHROMA_DATA_PATH = "chroma_data/content/"
        self.EMBED_MODEL = "all-MiniLM-L6-v2"
        self.COLLECTION_NAME = "competitors"
        self.client = chromadb.PersistentClient(path=self.CHROMA_DATA_PATH)
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=self.EMBED_MODEL)
        self.collection = self.client.get_or_create_collection(
            name=self.COLLECTION_NAME,
            embedding_function=self.embedding_func, 
            metadata={"hnsw:space": "cosine"} # Using cosine similarity as a measure for finding similar competitors
        )


    def drop_unwanted_columns_rows(self, input_file, output_file, category_type):

        columns_to_drop = ["artworkUrl512", "genres", "price", "primaryGenreId", "averageUserRating", "appId"]

        # Read the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Drop the unwanted columns
        df = df.drop(columns=columns_to_drop)

        # Filter the categories based on user input 
        df = df[df['primaryGenreName'] == category_type]

        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_file, index=False)

    def load_documents(self, csv_file):
        # Loading a csv file
        loader = CSVLoader(csv_file, encoding="utf-8")

        # Invokes the load() method of the loader object to load the documents from the CSV file.
        documents = loader.load()

        return documents

    def add_documents_to_collection(self, documents):
        # Adding the data into the vector database
        documents_as_strings = [doc.page_content for doc in documents]

        self.collection.add(
            documents=documents_as_strings,
            ids=[f"id{i}" for i in range(len(documents))]
        )

    def query_similar_documents(self, app_description, n_results=10):
        # Query to find competiros based on app description
        query_results = self.collection.query(
            query_texts=[f"Find the top app with similar app features for the following app description: {app_description}"],
            n_results=n_results
        )
        # Converting the distances from cosine distance to cosine similarity by subtracting one from the distance output then convert it into decimal number 
        final_distances = [round((1 - x)*100) for x in query_results["distances"][0]]

        # Adding the distance to the data
        connected_values = list(zip(query_results["documents"][0], final_distances))
        
        # Function to split tuples
        def split_tuple(tuple_value):
            description_pattern = r'description:([\s\S]*?)(?=\ :|\Z)'
            track_name_pattern = r'trackName:([\s\S]*?)primaryGenreName:'
            genre_name_pattern = r'primaryGenreName:([\s\S]*)'
            description_match = re.search(description_pattern, tuple_value[0])
            track_name_match = re.search(track_name_pattern, tuple_value[0])
            genre_name_match = re.search(genre_name_pattern, tuple_value[0])
            description = description_match.group(1).strip() if description_match else ""
            track_name = track_name_match.group(1).strip() if track_name_match else ""
            genre_name = genre_name_match.group(1).strip() if genre_name_match else ""


            similarity = tuple_value[1]

            return [(description, track_name, genre_name, similarity)]

        # Iterate through the list of tuples
        result = []
        for tuple_value in connected_values:
            result.extend(split_tuple(tuple_value))

        return result

    def write_to_csv(self, data, csv_file):
        # Write data to CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['description', 'trackName', 'primaryGenreName', 'similarity'])  # Write headers
            for item in data:
                writer.writerow([item[0], item[1], item[2], item[3]])  # Write each item into a row
            
        # Deleting the items in a collection
        self.collection.delete(
               ids=[f"id{i}" for i in range(len(documents))]
               )
        
        

# Example usage
processor = FindCompetitors()
input_file = "app_info.csv" #Getting the file from scraper 
output_file = "output1.csv"
# INPUT BY USER
category_type = "Book" 

processor.drop_unwanted_columns_rows(input_file, output_file, category_type)

documents = processor.load_documents(output_file)
processor.add_documents_to_collection(documents)

# INPUT BY USER
app_description = "Bookworm Haven is a feature-rich book app offering an extensive collection across genres. Enjoy personalized recommendations, customizable reading experience, bookmarks, and highlights."

query_results = processor.query_similar_documents(app_description, n_results=20)

csv_file = 'final_output1.csv'
processor.write_to_csv(query_results, csv_file)
from pymongo import MongoClient

class MongoOperator:
    def __init__(self, database_name):
        # Connect to MongoDB server running on localhost at port 27017
        self.client = MongoClient("localhost", 27017)

        # Access the specified database
        self.database = self.client[database_name]

    def create_collection(self, collection_name):
        # Create a new collection
        self.database.create_collection(collection_name)
        print(f"Collection '{collection_name}' created successfully.")

    def insert_document(self, collection_name, document):
        # Insert a single document into the specified collection
        collection = self.database[collection_name]
        result = collection.insert_one(document)
        print(f"Document inserted with ID: {result.inserted_id}")

    def insert_documents(self, collection_name, documents):
        # Insert a list of documents into the specified collection
        collection = self.database[collection_name]
        result = collection.insert_many(documents)
        print(f"{len(result.inserted_ids)} documents inserted successfully.")

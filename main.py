import json
from mongo_operations.mongo_operator import MongoOperator


if __name__ == "__main__":
    mongo_operator = MongoOperator("local")

    # Create a collection named "pokemon"
    mongo_operator.create_collection("pokemon_types")

    # Insert pokemon list in our pokemon collection
    pokemon_json = 'data/pokemon_types.json'
    with open(pokemon_json, 'r') as file:
        pokemon_data = file.read()
    
    pokemon_dict = json.loads(pokemon_data)

    mongo_operator.insert_documents(
        "pokemon_types", 
        pokemon_dict['pokemon_types']
    )
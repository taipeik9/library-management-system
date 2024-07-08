import os
from dotenv import load_dotenv

import pymongo
import json

if __name__ == "__main__":
    # For env variables
    load_dotenv()

    # Connect to Mongo Database called recipes
    db = pymongo.MongoClient(os.environ["MONGO_URL"]).recipes

    # Open json file to be sent to database
    with open("bonappetit.json") as f:
        documents = json.load(f)

    # Insert many recipes into the recipes collection within our previously opened database
    db.recipes.insert_many(documents)

    # Note: The database and collection are both called recipes (its confusing lmao)

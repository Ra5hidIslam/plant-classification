from flask import Flask, jsonify, abort,request
from pymongo import MongoClient
import os
from flask_cors import CORS
import urllib


# MongoDB connection setup
client = MongoClient("mongodb://mongodb:27017/")
db = client["plant_database"]
collection = db["plants"]

FILE_SERVER_URL_LOCAL = "http://localhost:5002/download-image/"    
FILE_SERVER_URL_DOCKER = "/api/files/download-image/"


app = Flask(__name__)

CORS(app)

# Sample route for plant recognition (after model recognition)
@app.route('/recognized-plant/', methods=['GET'])
def recognized_plant():
    encoded_query = request.args.get('query', '')
    # Decode the query string
    plant_name = urllib.parse.unquote(encoded_query)
    # Find the plant document from MongoDB
    plant = collection.find_one({"name": plant_name})
    # plant = collection.find_one({"name": "Peace lily"})
    print(f"the name of the plant is:{plant_name}")
    if not plant:
        abort(404, description="Plant not found")

    image_urls = [FILE_SERVER_URL_DOCKER + image['path'] for image in plant["images"]]
    print(image_urls)
    return jsonify({"plant_name": plant['name'], "image_paths": image_urls,"description":plant['description']})

if __name__ == '__main__':
    app.run(debug=True,port=5001,host ='0.0.0.0')
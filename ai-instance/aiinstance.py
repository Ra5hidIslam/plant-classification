#Server descrptions
#This server contains the ai model and the mongdb instance to serve the plant data. 



#importing the dependencies
import tensorflow as tf
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras import models
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os
from flask_cors import CORS
from dotenv import load_dotenv
ENV = os.getenv("APP_ENV", "development")

if ENV == "production":
    load_dotenv("/home/rashid/Code/Plant Classification Final Docker/.env.production")
else:
    load_dotenv("/home/rashid/Code/Plant Classification Final Docker/.env.development")



app = Flask(__name__)

CORS(app)
# Load the model
p_c_model_path = os.getenv("MODEL_PATH")
# p_c_model_path = "/home/rashid/Code/Plant Classification Final Docker/Data/Models/model.keras"
# p_c_model_path = "/app/data/Models/model.keras"
print(f"model path={p_c_model_path}")
try:
    p_c_model = load_model(p_c_model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load the model at {p_c_model_path}: {str(e)}")

# Define class names
class_file_path = os.getenv("CLASS_PATH")
with open(class_file_path,"r") as file:
    class_names=  file.read()
class_names = class_names.split(",")
# print(class_names)
# # class_names=  class_names[:-1]
# print(class_names)

def prepare_single_image_for_classification(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)  # Converting to grayscale for lowering the load on
    image = tf.image.resize(image, [224,224])  # Resize to required size if necessary
    image = tf.keras.applications.efficientnet.preprocess_input(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save and preprocess the image
    uploads_path = os.getenv("UPLOADS_PATH")
    file_path = os.path.join(uploads_path, file.filename)
    file.save(file_path)

    img_array = prepare_single_image_for_classification(file_path)
    
    # Make prediction
    predictions = p_c_model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)-1]
    # print(f"predicted class:{predicted_class}")   

    return jsonify({'predicted_class': predicted_class})

#route to get the, think about using dynamic routes so I don't have to create different routes for extracting different information
#requirements:
#plant images
#plant description
if __name__ == '__main__':
    app.run(debug=True,port=5003,host='0.0.0.0')

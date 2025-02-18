from flask import Flask, send_file, abort,request
import os
import mimetypes
from flask_cors import CORS
from dotenv import load_dotenv
ENV = os.getenv("APP_ENV", "development")

if ENV == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env.development")


IMAGES_DIR  = os.getenv("IMAGES_PATH")
  # Update with the correct directory

app = Flask(__name__)

CORS(app)   

@app.route('/download-image/<path:image_path>', methods=['GET'])
def download_image(image_path):
    # data =  request.json()
    image_path = os.path.join(IMAGES_DIR, image_path)
    full_path = os.path.abspath(image_path)
    if not full_path.startswith(IMAGES_DIR):
        abort(403,description = "Access Denied")
    # print(f"data = {data}")
    # print(f"does Image path exist :{os.path.exists(image_path)}")
    if not os.path.exists(image_path):
        abort(404, description="Image not found")
    
    mime_type, _ = mimetypes.guess_type(image_path)
    
    return send_file(image_path, mimetype=mime_type)  # Adjust MIME type as needed

if __name__ == '__main__':
    app.run(debug=True,port=5002,host='0.0.0.0')
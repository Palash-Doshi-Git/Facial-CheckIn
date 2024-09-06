import base64
import json
import os
import cv2
import numpy as np
from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
import azureSqldatabase
import main

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = 'images'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Directory to save images
        upload_folder = os.path.join(os.getcwd(), 'images')

        # Create directory if it doesn't exist
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Check if an image is part of the request
        if 'image' not in request.files:
            return jsonify({"error": "No image part in the request"}), 400

        file = request.files['image']

        # Check if the file has a filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # Save the image to the "images" directory
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)

        # Upload the file to Blob Storage
        blob_client = main.container_client.get_blob_client(file.filename)
        main.upload_all_images_to_blob()

        return jsonify({"success": "Image uploaded successfully"}), 200

    except Exception as e:
        # Print the error to the console for debugging
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during image upload"}), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload_frame", methods=['POST'])
def upload_frame():
    azureSqldatabase.create_table()
    data = request.get_json()
    image_data = data.get('image')

    # Decode base64 image data
    image_data = base64.b64decode(image_data.split(',')[1])
    np_image = np.frombuffer(image_data, dtype=np.uint8)
    frame = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    print("Hitting Server")
    # Call your process_video function
    result = main.process_video(frame)

    return json.dumps(
        result
    )


@app.route('/check-attendance', methods=['GET'])
def check_attendance():
    try:
        # Fetch all attendance records from the database
        records = azureSqldatabase.get_all_attendance_records()
        print(records)
        # Render the result.html template and pass the records
        return render_template('result.html', records=records)
    except Exception as e:
        print(f"Error: {e}")
        return "Error checking attendance", 500


@app.route('/delete-sql-data', methods=['POST'])
def delete_sql_data():
    azureSqldatabase.delete_all_records()  # Call the function to delete all SQL records
    return "All SQL database records have been deleted."


@app.route('/delete-blob-data', methods=['POST'])
def delete_blob_data():
    main.delete_all_blobs()  # Call the function to delete all Blob storage data
    return "All Azure Blob storage data has been deleted."


@app.route('/list-blobs', methods=['GET'])
def list_blobs():
    try:
        # Fetch the list of blob names from Azure Blob Storage
        blob_list = main.get_blob_names()  # Ensure you have this method in your main.py
        return jsonify(blob_list), 200
    except Exception as e:
        print(f"Error occurred while listing blobs: {e}")
        return jsonify({"error": "An error occurred while listing blobs"}), 500


if __name__ == '__main__':
    app.run(debug=True)

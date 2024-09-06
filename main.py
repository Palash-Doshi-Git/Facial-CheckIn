import base64
import os
from datetime import datetime

import cv2
import face_recognition
import numpy as np
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

import azureSqldatabase

# Initialize the connection to Azure Blob Storage
load_dotenv()

connect_str = os.getenv('AZURE-STORAGE-CONN-STR')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = 'student-images'
container_client = blob_service_client.get_container_client(container_name)
file_path = 'images'
blob_name = os.path.basename(file_path)  # Get the file name for the blob
blob_client = container_client.get_blob_client(blob_name)

if not container_client.exists():
    container_client.create_container()


def upload_all_images_to_blob(directory_path='images'):

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('jpg', 'jpeg', 'png')):
            file_path = os.path.join(directory_path, filename)
            blob_client = container_client.get_blob_client(filename)

            try:
                # Check if the blob already exists
                if blob_client.exists():
                    continue

                # Upload the file to Blob Storage
                with open(file_path, "rb") as data:
                    blob_client.upload_blob(data, overwrite=True)
                    print(f"Uploaded {filename} successfully.")
            except Exception as e:
                print(f"Failed to upload {filename}: {e}")


def load_known_faces():
    upload_all_images_to_blob()
    images = []
    person_names = []
    my_list = os.listdir('images')
    for cu_img in my_list:
        if cu_img.endswith(('jpg', 'jpeg', 'png')):
            current_img = cv2.imread(f'images/{cu_img}')
            images.append(current_img)
            person_names.append(os.path.splitext(cu_img)[0])
    return person_names, face_encodings(images)


def face_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


def process_video(frame):
    person_names, encode_list_known = load_known_faces()
    result = "No face recognized"

    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
    faces_current_frame = face_recognition.face_locations(faces)
    encodes_current_frame = face_recognition.face_encodings(faces, faces_current_frame)

    for encodeFace, faceLoc in zip(encodes_current_frame, faces_current_frame):
        matches = face_recognition.compare_faces(encode_list_known, encodeFace)
        face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
        match_index = np.argmin(face_dis)

        if matches[match_index]:
            name = person_names[match_index].upper()
            dtstring = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            result = f"Attendance marked for {name} at {dtstring}"
            check_name_state(name, dtstring)

            # Draw rectangle around the face
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            break

    # Encode the frame to be sent back to frontend
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    return {"result": result, "frame": jpg_as_text}


def check_name_state(name, dtstring):
    if azureSqldatabase.exist_name(name):
        azureSqldatabase.update_data(name, dtstring)
    else:
        azureSqldatabase.insert_data(name, dtstring)


def get_blob_names():
    blob_names = [blob.name for blob in container_client.list_blobs()]
    blob_names = [name.rsplit('.', 1)[0] for name in blob_names] # trim .jpg from names
    return blob_names


def delete_all_blobs():
    blobs = container_client.list_blobs()
    for blob in blobs:
        blob_del_client = container_client.get_blob_client(blob.name)
        blob_del_client.delete_blob()

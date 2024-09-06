import base64
import os
from azure.communication.email import EmailClient
from dotenv import load_dotenv

load_dotenv()


def send_email_with_attachment(file_path, email):
    try:
        # Initialize the EmailClient with the connection string
        connection_string = os.getenv("ACS_CONNECTION_STRING")  # Replace with your ACS connection string
        client = EmailClient.from_connection_string(connection_string)
        sender_address = os.getenv('senderAddress')

        # Read the Excel file to attach
        with open(file_path, 'rb') as file:
            file_content = file.read()

        # Create the email message
        message = {
            "senderAddress": sender_address,  # Replace with your verified sender email
            "recipients": {
                "to": [{"address": email}]  # Replace with recipient email
            },
            "content": {
                "subject": "Excel Report",
                "plainText": "Please find the attached Excel report."
            },
            "attachments": [
                {
                    "contentInBase64": base64.b64encode(file_content).decode('utf-8'),  # Updated key
                    "contentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "name": os.path.basename(file_path)
                }
            ]
        }

        # Send the email message
        poller = client.begin_send(message)
        result = poller.result()  # Wait for the sending operation to complete

        return result

    except Exception as ex:
        print(f"An error occurred: {ex}")

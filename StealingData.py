import json
import streamlit as st
from azure.storage.blob import BlobServiceClient

def load_data_from_azure():
    connection_string = st.secrets['AZURE_STORAGE_CONNECTION_STRING']
    container_name = "personal"
    blob_name = "student_data 23-24.json"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    blob_data = blob_client.download_blob().readall()
    return json.loads(blob_data)


data = load_data_from_azure()
print(data)
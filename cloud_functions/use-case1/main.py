import functions_framework
from google.cloud import storage
from PIL import Image
import io

# Inicializa o cliente do Cloud Storage
storage_client = storage.Client()

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def convert_image(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket_name = data["bucket"]
    file_name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket_name}")
    print(f"File: {file_name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    if file_name.endswith('.png'):
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        image_data = blob.download_as_bytes()        

        # Converter PNG para JPEG
        with Image.open(io.BytesIO(image_data)) as img:
            img = img.convert("RGB")
            output_buffer = io.BytesIO()
            img.save(output_buffer, format="JPEG")
            output_buffer.seek(0)

        # Salvar a nova imagem no mesmo bucket com extensão .jpg
        new_file_name = file_name.replace('.png', '.jpg')
        new_blob = bucket.blob(new_file_name)
        new_blob.upload_from_file(output_buffer, content_type="image/jpeg")

        print(f"Imagem convertida e salva como {new_file_name}")
    else:
        print(f"Ignorando {file_name}, pois não é um arquivo PNG.")
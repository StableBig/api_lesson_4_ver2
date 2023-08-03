import os
import requests
from urllib.parse import urlparse


def get_file_extension_from_url(url):
    parsed_url = urlparse(url)
    file_extension = os.path.splitext(parsed_url.path)[1]
    return file_extension


def download_image(image_url, save_folder, filename_prefix, timestamp, index):
    image_extension = get_file_extension_from_url(image_url)
    image_name = f"{filename_prefix}_{timestamp}_{index}{image_extension}"
    save_path = os.path.join(save_folder, image_name)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(save_path, "wb") as file:
        file.write(response.content)

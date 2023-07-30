import os
import requests

def download_image_from_url(image_url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(image_url, headers=headers)
    response.raise_for_status()

    with open(save_path, "wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    save_path = "images/hubble.jpeg"

    download_image_from_url(image_url, save_path)
    print(f"Изображение скачано и сохранено здесь: {save_path}")

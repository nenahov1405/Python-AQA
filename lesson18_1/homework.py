import requests
import os

def upload_image_to_server(base_url, filepath):
    filename = os.path.basename(filepath)
    print(f'URL for POST request: {base_url}')

    with open(filepath, 'rb') as f:
        files = {
            "image": (filename, f)
        }
        resp = requests.post(base_url, files=files)
        return resp

def get_image_from_server(full_url, filepath):
    headers = {"Content-Type": "image"}
    resp = requests.get(url=full_url, headers=headers, stream=True)

    if resp.status_code == 200:
        with open(filepath, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"File successfully saved to: {filepath}")
    else:
        print(f"Download failed. Status Code: {resp.status_code}")

    return resp

def delete_image_on_server(base_url, filename):
    # URL encode
    encoded_filename = requests.utils.quote(filename)
    delete_url = f"{base_url}/{encoded_filename}"

    print(f"Sending DELETE to: {delete_url}")
    resp = requests.delete(delete_url)

    if resp.status_code == 200:
        print("File successfully deleted on server")
        print("Server message:", resp.json().get("message"))
    else:
        print(f"Delete failed. Status Code: {resp.status_code}")
        print(resp.text)

    return resp


base_upload_url = "http://127.0.0.1:8080/upload"
file_relative_path = os.path.join("post", "test_image1.png")
base_dir = os.path.dirname(os.path.abspath(__file__))
full_file_path = os.path.join(base_dir, file_relative_path)

print(f"Full file path used: {full_file_path}")

try:
    #Завантаження зображення
    response = upload_image_to_server(base_upload_url, full_file_path)
    print(f"Status Code: {response.status_code}")
    print(f"Server Response: {response.text}")

    server_image_url = response.json().get('image_url')
    server_image_url = server_image_url.replace('/uploads/', '/image/')
    filename = os.path.basename(server_image_url)
    path_for_saving = (
        f"/Users/kyrylo.nenakhov/PycharmProjects/Python-AQA/lesson18_1/get/{filename}"
    )

    #Отримання зображення
    response = get_image_from_server(server_image_url, path_for_saving)
    print(f"Status Code: {response.status_code}")

    #Видалення зображення
    delete_base_url = "http://127.0.0.1:8080/delete"
    delete_image_on_server(delete_base_url, filename)

except Exception as e:
    print(f"An error occurred: {e}")
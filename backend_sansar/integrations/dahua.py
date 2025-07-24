# integrations/dahua.py
import requests
import base64

def add_face(device_ip: str, login: str, password: str, photo_base64: str, person_id: str):
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    data = {
        "action": "addFace",
        "personId": person_id,
        "faceData": photo_base64
    }
    response = requests.post(f"http://{device_ip}/cgi-bin/accessControl.cgi", headers=headers, json=data)
    return response.json()
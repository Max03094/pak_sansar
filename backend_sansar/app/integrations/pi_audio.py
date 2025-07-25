# integrations/pi.py
import requests

def play_audio(pi_ip, mp3):
    requests.post(f"http://{pi_ip}/play", json={"file": mp3})
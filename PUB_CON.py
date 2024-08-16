import subprocess
import threading
import requests
import json
import sys
from time import sleep

def create_public_connection():
    command = "./ngrok tcp 8089"
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def CRT_PUB_CON():
    publicthread = threading.Thread(target=create_public_connection)
    publicthread.start()
    sleep(1)
    
    get_data_url = ""
    try:
        get_data_req = requests.get(get_data_url)
        if get_data_req.status_code == 200:
            data = get_data_req.text
            json_data = json.loads(data)
            public_url = json_data['tunnels'][0]['public_url']
            # Ngrok URL'sini doğrudan kullan
            return public_url
        else:
            print("Failed to create public connection...")
            print("Try again")
            sys.exit()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit()

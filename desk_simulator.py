import random
import time
import requests

FIREBASE_URL = 'https://smart-desk-occupancy-tracker-default-rtdb.firebaseio.com/desks.json'

def send_status(desk_name, occupied):
    data = {desk_name: {"occupied": occupied}}
    response = requests.patch(FIREBASE_URL, json=data)
    print(f"Sent: {data} → {response.status_code}")

while True:
    for i in range(1, 4):
        status = random.choice([True, False])
        send_status(f"desk{i}", status)
    time.sleep(5)

import time
import requests

# Hii ni URL ya API yako ya Django inayopokea data
url = "http://127.0.0.1:8000/api/location/update/"

# Hizi ni taarifa za mfano za simu na eneo lake
data = {
    "device": "Simu_Ya_Mkononi_01",
    "latitude": -6.7924,
    "longitude": 39.2083,
    "taifa": "Tanzania",
    "mkoa": "Dar es Salaam",
    "wilaya": "Ilala",
    "kata": "Kivukoni",
    "mtaa": "Posta"
}

print("Inaanza kutuma eneo la kifaa kiotomatiki...")

while True:
    try:
        # Tunatuma ombi la POST kwenda kwenye API yako
        response = requests.post(url, data=data)

        if response.status_code == 200 or response.status_code == 201:
            print("Eneo limetumwa na kuhifadhiwa kwa mafanikio!")
        else:
            print("Imeshindwa kutuma:", response.text)

    except Exception as e:
        print("Hitilafu ya mtandao au seva:", e)

    # Inasubiri sekunde 10 kabla ya kutuma tena
    time.sleep(10)

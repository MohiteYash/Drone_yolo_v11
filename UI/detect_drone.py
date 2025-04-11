from ultralytics import YOLO
import requests
import os
from telegram_config import BOT_TOKEN, CHAT_ID

# Load model
model = YOLO("Final_drone.pt")

def send_telegram_alert(image_path=None):
    message = "🚨 Alert: A drone has been detected!"

    # Send text alert
    send_text_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(send_text_url, data=data)

    # Send image if available
    if image_path:
        send_photo_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(image_path, "rb") as photo:
            files = {"photo": photo}
            data = {"chat_id": CHAT_ID}
            requests.post(send_photo_url, data=data)

def detect_drone(image):
    results = model(image)
    names = model.names
    save_path = "output.jpg"
    results[0].save(filename=save_path)

    # Check if 'drone' detected
    for result in results:
        for box in result.boxes.data:
            cls = int(box[-1])
            if names[cls].lower() == "drone":
                send_telegram_alert(save_path)
                return save_path, "Drone Detected 🚨"
    return save_path, "No Drone Detected ✅"

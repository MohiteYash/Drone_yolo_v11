import cv2
from ultralytics import YOLO
import time
import requests
import os

# Load YOLOv8 custom model
model = YOLO("Final_drone.pt")
names = model.names  # class names

# Telegram Bot credentials
BOT_TOKEN = '8140564783:AAHC9qOUwWBccIxjaGFvxScyiCs2bH6Clqc'     # Replace this
CHAT_ID = '1165989207'         # Replace this

# Android IP Webcam stream URL
ip_webcam_url = "http://192.168.1.43:4747/video"  # Updated to your actual DroidCam port

def send_telegram_alert(image_path):
    """Sends an image to Telegram."""
    message = "🚨 Drone Detected!"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, 'rb') as img:
        requests.post(url, data={"chat_id": CHAT_ID, "caption": message}, files={"photo": img})

def main():
    cap = cv2.VideoCapture(ip_webcam_url)

    if not cap.isOpened():
        print("[ERROR] Could not open video stream.")
        return

    print("[INFO] Starting drone detection with live view...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to capture frame.")
            break

        # Run detection
        results = model(frame)
        detected = False

        for box in results[0].boxes.data:
            cls = int(box[-1])
            if names[cls].lower() == "drone":
                detected = True
                break

        # Save alert and send Telegram message
        if detected:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            output_path = f"detection_{timestamp}.jpg"
            frame_with_boxes = results[0].plot()  # Draw boxes on frame
            cv2.imwrite(output_path, frame_with_boxes)
            send_telegram_alert(output_path)
            print(f"[ALERT] Drone detected at {timestamp} 🚨")
            time.sleep(10)  # Cooldown to prevent multiple alerts
        else:
            frame_with_boxes = results[0].plot()

        # Show the frame in a window
        cv2.imshow("Drone Detection Live Feed", frame_with_boxes)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

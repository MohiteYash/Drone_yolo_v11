
# Drone Detection System Deployment on Raspberry Pi 3 B

This documentation explains how to deploy a YOLOv11n-based drone detection system on a Raspberry Pi 3 B running Debian Bullseye 64-bit. The setup includes SSH, VNC access, a virtual environment, required library installation, file transfers, camera setup, and real-time detection with alerting.

Hardware & Software Requirements:
- Raspberry Pi 3 B
- MicroSD card (8 GB or more)
- USB Webcam
- Laptop or Desktop (for setup and file transfers)
- Raspberry Pi OS: Debian Bullseye 64-bit (Lite or Full)
- Internet connection via 2.4GHz Wi-Fi

Step-by-Step Deployment Process:

1. Flash Raspberry Pi OS
- Use Raspberry Pi Imager to flash Debian Bullseye 64-bit onto the SD card.
- Enable SSH and Wi-Fi in advanced settings.
- Insert the SD card into the Raspberry Pi and power it on.

2. First-Time Setup
- Access Raspberry Pi using PuTTY.
- Enable VNC via `sudo raspi-config` > Interface Options > VNC > Enable.
- Use VNC Viewer on your laptop to view the Pi's GUI.

3. Update & Upgrade the System
```bash
sudo apt update && sudo apt upgrade -y
```

4. Create Project Directory and Virtual Environment
```bash
mkdir drone
cd drone
python3 -m venv venv
source venv/bin/activate
```

5. Install Required Libraries
```bash
pip install --upgrade pip
pip install ultralytics opencv-python pillow
```

6. Transfer Code and Model Files via SCP
```bash
scp -r path\to\your\project pi@<raspberry_pi_ip>:~/drone/
```

7. Connect and Configure USB Camera
```bash
sudo apt install fswebcam
fswebcam test.jpg
sudo apt install libopencv-dev python3-opencv
```

8. Real-Time Detection Script Execution
```bash
cd ~/drone
source venv/bin/activate
python detect_camera.py
```

Real-Time Alerting System:
- Use Telegram Bot API or Email (SMTP) to send alerts upon drone detection.
- Ensure your script handles webcam input and detection alerts.

Summary:
- Flash OS, enable SSH/VNC, setup Pi
- Install Python packages in a virtual environment
- Transfer code and run the detection script
- Use camera + detection + alerts

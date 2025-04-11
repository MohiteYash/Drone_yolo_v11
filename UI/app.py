import gradio as gr
from detect_drone import detect_drone
from PIL import Image

def inference(image):
    result_path, status = detect_drone(image)
    return Image.open(result_path), status

app = gr.Interface(
    fn=inference,
    inputs=gr.Image(type="filepath", label="Upload Image"),
    outputs=[gr.Image(label="Detection Output"), gr.Text(label="Detection Status")],
    title="🚁 Drone Detection System",
    description="Upload an image to check for drone presence. Sends a Telegram alert with detection snapshot if a drone is found."
)

app.launch()


import gradio as gr
import cv2
import numpy as np

def sketch_image(image):
    """Converts an image to a pencil sketch."""
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image
    
    # Apply a Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred_image = 255 - blurred_image
    
    # Create the pencil sketch image by dividing the grayscale image by the inverted blurred image
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    return pencil_sketch

# Create the Gradio interface
iface = gr.Interface(
    fn=sketch_image,
    inputs=gr.Image(type="numpy", label="Upload an image"),
    outputs=gr.Image(type="numpy", label="Sketch"),
    title="Image to Sketch Converter",
    description="Drag and drop an image to convert it into a pencil sketch.",
    allow_flagging="never"
)

# Launch the app
iface.launch()

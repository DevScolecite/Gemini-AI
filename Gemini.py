import os
import google.generativeai as genai
import PIL.Image

# Configure your Gemini API key
api_key = os.environ.get("AIzaSyCmTFXRc4lvuguHnyqyB15AjYkAu_FJ29Q")
if not api_key:
    raise ValueError("AIzaSyCmTFXRc4lvuguHnyqyB15AjYkAu_FJ29Q")

genai.configure(api_key=api_key)

# Load the image
image_path = 'path/to/image.png'  # Replace with your image path
img = PIL.Image.open(image_path)

# Create the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Generate content based on the image
response = model.generate_content(["What is in this photo?", img])

# Print the generated response
if response:
    print(response[0].get('text', ''))
else:
    print("I'm sorry, I couldn't process that request.")

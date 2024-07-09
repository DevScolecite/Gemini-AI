import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image

# Load environment variables from gemini.env file
load_dotenv(dotenv_path='gemini.env')

# Configure your Gemini API key
api_key = os.environ.get("GOOGLE_API_KEY")
print(f"API Key: {api_key}")  # Debugging line to print the API key

if not api_key:
    raise ValueError("Please set your GOOGLE_API_KEY environment variable")

genai.configure(api_key=api_key)

# Load the image
image_path = 'path/to/image.png'  # Replace with your image path
try:
    img = PIL.Image.open(image_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Image file not found at {image_path}")

# Create the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Generate content based on the image
try:
    response = model.generate_content(["What is in this photo?", img])
    if response:
        print(response[0].get('text', ''))
    else:
        print("I'm sorry, I couldn't process that request.")
except Exception as e:
    print(f"An error occurred during content generation: {e}")

import requests
import io
from PIL import Image
import base64
import json
import os

# API configuration
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {"Authorization": "Bearer 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"}  # Your API key


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Ask the user for a prompt
user_prompt = input("Enter a prompt for image generation: ")

# Query the model for an image based on the user's input
image_data = query({
    "inputs": user_prompt,
})

# Check if data is returned
if image_data:
    try:
        # Check if the response is JSON (base64 encoded image)
        if image_data.startswith(b'{'):
            json_data = json.loads(image_data)
            img_str = json_data.get("generated_image", "")
            if img_str:
                image = Image.open(io.BytesIO(base64.b64decode(img_str)))
            else:
                print("No image found in response.")
        else:
            # If it's raw image bytes, open it directly
            image = Image.open(io.BytesIO(image_data))

        # Clean the user input to make it safe for file naming
        valid_filename = "".join(c for c in user_prompt if c.isalnum() or c in (' ', '_')).rstrip()
        image_path = f"{valid_filename}.png"  # Save the image as a PNG file

        # Save the image
        image.save(image_path)
        print(f"Image saved successfully as '{image_path}'")

        # Open the image in the default image viewer
        image.show()  # This will open the saved image

    except Exception as e:
        print(f"Could not open or save image: {e}")
        print(f"Raw response: {image_data}")
else:
    print("Failed to retrieve image.")
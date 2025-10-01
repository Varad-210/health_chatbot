import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API token from the environment
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# The URL for the model we want to use
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

# Check if the API token is available
if not API_TOKEN:
    print("Hugging Face API token not found. Please set the HUGGINGFACE_API_TOKEN environment variable.")
    headers = None
else:
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

def get_huggingface_response(user_message):
    """
    Gets a response from the Hugging Face Inference API.
    """
    if not headers:
        return "Hugging Face client could not be initialized. Please check your API token."

    try:
        # Make the API call
        response = requests.post(API_URL, headers=headers, json={
            "inputs": {
                "text": user_message
            },
        })

        # Check for a successful response
        if response.status_code == 200:
            # The response is a list, we want the generated_text from the first item
            return response.json()['generated_text']
        elif response.status_code == 503: # Model is loading
            return "The AI model is loading, please try again in a moment..."
        else:
            return f"Error: Received status code {response.status_code} from Hugging Face API."

    except Exception as e:
        print(f"An error occurred with the Hugging Face API: {e}")
        return "Sorry, I'm having trouble connecting to the AI service right now."

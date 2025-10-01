from google.cloud import translate_v2 as translate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# IMPORTANT: You need to set up Google Cloud Translation API and get an API key.
# Create a .env file in the root of the project and add the following line:
# GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"

# Initialize the Translation client
# The client will automatically use the credentials from the .env file.
try:
    translate_client = translate.Client()
except Exception as e:
    print("Could not initialize Google Translate client. Please check your API key and credentials.")
    print(e)
    translate_client = None

def translate_text(text, target_language):
    """Translates text into the target language."""
    if not translate_client:
        return f"[Translation disabled] {text}"

    try:
        result = translate_client.translate(text, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        print(f"Error during translation: {e}")
        return f"[Translation error] {text}"

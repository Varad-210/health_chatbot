
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the project root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path=dotenv_path)

# Get the API key from the environment
# IMPORTANT: Make sure you have an .env file with your OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if not api_key:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    client = None
else:
    client = OpenAI(api_key=api_key)

# Language map to convert code to full name
language_map = {
    'hi': 'Hindi',
    'es': 'Spanish',
    'fr': 'French',
    'en': 'English'
}

def get_openai_response(user_message, language_code='en'):
    """
    Gets a response from the OpenAI API based on the user message and language.
    """
    if not client:
        return "OpenAI client could not be initialized. Please check your API key."

    language_name = language_map.get(language_code, 'English')

    # This is the system prompt that tells the AI how to behave.
    system_prompt = f"""
    You are a helpful and empathetic public health chatbot.
    Your goal is to provide clear, safe, and supportive health information.
    - Always prioritize user safety.
    - If the user mentions symptoms like 'fever', 'headache', or feeling sick, your primary response should be to advise them to consult a real doctor or visit a clinic. Do not attempt to diagnose.
    - You can provide general information on topics like vaccines, hand washing, and immunity.
    - Keep your responses concise and easy to understand.
    - You must respond in the following language: {language_name}.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,  # Adjust for more or less creative responses
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred with the OpenAI API: {e}")
        return "Sorry, I'm having trouble connecting to the AI service right now."

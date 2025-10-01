import json
import os

# Construct the absolute path to responses.json
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
responses_path = os.path.join(base_dir, 'data', 'responses.json')

with open(responses_path, 'r') as f:
    responses = json.load(f)

def get_response(message):
    message = message.lower()
    if 'fever' in message:
        return responses.get('fever', responses['default'])
    elif 'vaccine' in message:
        return responses.get('vaccine', responses['default'])
    elif 'hand wash' in message:
        return responses.get('hand_wash', responses['default'])
    elif 'immunity' in message:
        return responses.get('immunity', responses['default'])
    else:
        return responses['default']

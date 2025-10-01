from flask import Blueprint, request, jsonify
from backend.services.huggingface_engine import get_huggingface_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # Get the response from the new Hugging Face engine
    response = get_huggingface_response(user_message)

    return jsonify({'response': response})

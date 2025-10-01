from flask import Flask, send_from_directory
from backend.routes.chatbot_routes import chatbot_bp
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Register the chatbot blueprint
app.register_blueprint(chatbot_bp, url_prefix='/api')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)

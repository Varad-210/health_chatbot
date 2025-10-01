# Health Chatbot

This is a web-based chatbot that answers health-related questions in multiple languages. It uses large language models to provide informative and helpful responses.

## Features

*   **Interactive Chat Interface:** A simple and intuitive chat interface to interact with the chatbot.
*   **Multi-language Support:** The chatbot can understand and respond in multiple languages, including English, Hindi, Spanish, and French.
*   **Powered by Large Language Models:** The chatbot uses powerful language models to understand and respond to user queries.

## Tech Stack

*   **Frontend:** HTML, CSS, JavaScript
*   **Backend:** Python, Flask
*   **APIs:** OpenAI

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Varad-210/health_chatbot
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd health_chatbot
    ```
3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
5.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key"
    ```
7.  **Run the Flask server:**
    ```bash
    python backend/app.py
    ```
8.  **Open the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

## File Structure

```
health-chatbot/
├── backend/
│   ├── app.py              # Flask application
│   ├── routes/
│   │   └── chatbot_routes.py # Chatbot API routes
│   └── services/
│       ├── openai_engine.py  # OpenAI API integration
│       └── ...
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── script.js           # Frontend JavaScript
│   └── styles.css          # CSS styles
├── .env.example            # Example environment file
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## How to Use

1.  Open the web interface in your browser.
2.  Select your preferred language from the language dropdown.
3.  Type your health-related question in the message input box and press Enter or click the send button.
4.  The chatbot will provide a response in the chat interface.

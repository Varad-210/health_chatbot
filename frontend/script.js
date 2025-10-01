document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.querySelector('.message-input');
    const sendButton = document.querySelector('.send-button');
    const chatInterface = document.querySelector('.chat-interface');
    const languageDropdown = document.querySelector('.language-dropdown');

    // Coded language names to match Google Translate API
    const languageMap = {
        'English': 'en',
        'हिन्दी': 'hi',
        'Español': 'es',
        'Français': 'fr'
    };

    let currentLanguage = 'hi'; // Default language

    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const messageText = messageInput.value.trim();
        if (messageText === '') return;

        // Add user message to chat
        addMessage(messageText, 'user-message');
        messageInput.value = '';

        // Send message to backend
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: messageText, language: currentLanguage })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, 'bot-message');
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Sorry, something went wrong.', 'bot-message');
        });
    }

    function addMessage(text, type) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-bubble', type);
        messageElement.textContent = text;
        chatInterface.appendChild(messageElement);
        chatInterface.scrollTop = chatInterface.scrollHeight; // Auto-scroll to bottom
    }

    // Language selection logic (basic example)
    // In a real app, this would be a more complex dropdown.
    languageDropdown.addEventListener('click', () => {
        // Simple toggle for demonstration
        const newLang = languageDropdown.textContent.includes('हिन्दी') ? 'English' : 'हिन्दी';
        const newLangCode = languageMap[newLang];
        languageDropdown.textContent = `Language: ${newLang}`;
        currentLanguage = newLangCode;
        addMessage(`Language changed to ${newLang}`, 'bot-message');
    });
});

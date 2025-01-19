/*document.getElementById('send-btn').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div>User: ${userInput}</div>`;
    chatBox.innerHTML += `<div>Bot: ${data.reply}</div>`;
});*/

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // Get references to the input field, send button, and chat display area
    const userinput = document.getElementById('userinput'); // The input box for user's message
    const sendButton = document.getElementById('sendbtn'); // The "Send" button
    const chatDisplay = document.getElementById('chatbox'); // The area to display chat messages

    // Add an event listener to the send button
    sendButton.addEventListener('click', () => {
        const message = userinput.value.trim(); // Get and trim user input

        // Check if the input is not empty
        if (message === '') {
            alert('Please enter a message.');
            return;
        }

        // Append the user's message to the chat display
        appendMessage('You', message);

        // Clear the input field
        userinput.value = '';

        // Send the message to the backend
        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }), // Send user input as JSON
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                // Append the chatbot's response to the chat display
                appendMessage('Bot', data.reply);
            })
            .catch((error) => {
                console.error('Error:', error);
                appendMessage('Bot', 'Something went wrong. Please try again.');
            });
    });

    /**
     * Function to append a message to the chat display
     * @param {string} sender - The sender of the message ('You' or 'Bot')
     * @param {string} message - The message text
     */
    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message';
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatDisplay.appendChild(messageElement);

        // Scroll to the bottom of the chat display
        chatDisplay.scrollTop = chatDisplay.scrollHeight;
    }
});



















/*document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    function addMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${sender}`;
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Display user message
        addMessage(message, "user");
        userInput.value = "";

        try {
            // Send message to the backend
            const response = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message }),
            });
            const data = await response.json();

            // Display bot response
            addMessage(data.response, "bot");
        } catch (error) {
            console.error("Error:", error);
            addMessage("Something went wrong. Please try again.", "bot");
        }
    }

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });
});*/

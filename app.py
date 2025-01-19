'''import os
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
from flask import Flask, request, jsonify

genai.configure(api_key="AIzaSyAKUJS8gRzqPGwonKdkcMMBd2v1r64X-HE")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
'''
'''def speak_text(text):
    """
    Use gTTS to speak the given text.
    """
    tts = gTTS(text=text, lang='en', slow=False)
    # Save the speech to a temporary file
    tts.save("response1.mp3")
    # Save to system
    os.system("response1.mp3")'''

'''def listen_to_voice():
    """
    Capture audio from the microphone and convert it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=60)  # Listen for 60 seconds
            text = recognizer.recognize_google(audio)  # Use Google's STT
            return text
        except sr.WaitTimeoutError:
            return "No speech detected, try again."
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"'''

'''def get_gemini_response(user_input):
    """
    Send user input to the Gemini model and return its response.
    """
    response = chat_session.send_message(user_input)
    return response.text if response else "No response received."'''

# Main chatbot loop
'''while True:
    print("\nSay 'exit' or 'quit' to end the chat.")
    #user_input = listen_to_voice()  # Capture voice input
    user_input = ("Who are skydivers?")
    print(f"You: {user_input}")

    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat")
        #speak_text("Goodbye! Have a great day!")
        break

    if "No speech detected" in user_input or "Sorry" in user_input:
        print("Bot: Please try speaking again.")
        #speak_text("Please try speaking again.")
        continue'''

'''user_input = ("Who are skydivers?")
    # Get the bot's response
response = get_gemini_response(user_input)
print(f"Bot: {response}")
    #speak_text(response)


app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Replace this with a call to Google Gemini API
    chatbot_response = "Hello, this is the chatbot's response!"
    return jsonify({"reply": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)'''

import os
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Google Gemini API
genai.configure(api_key="AIzaSyB8t8jlQx7a4HP29dkBPO1_6opcXPt9IdY")

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 512,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(history=[])


def get_gemini_response(user_input):
    try:
        response = chat_session.send_message(user_input)
        return response.text if response else "No response received from the bot."
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        return "Something went wrong while connecting to the chatbot service."

def listen_to_voice():
    """
    Capture audio from the microphone and convert it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=60)  # Listen for 60 seconds
            text = recognizer.recognize_google(audio)  # Use Google's STT
            return text
        except sr.WaitTimeoutError:
            return "No speech detected, try again."
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user input from the request
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"reply": "Please provide a message."})

        # Get response from the Gemini model
        bot_response = get_gemini_response(user_input)

        return jsonify({"reply": bot_response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Something went wrong. Please try again."})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

    

'''def get_gemini_response(user_input):
    """
    Send user input to the Gemini model and return its response.
    """
    response = chat_session.send_message(user_input)
    return response.text if response else "No response received."

user_input = ("Who are skydivers?")
    # Get the bot's response
response = get_gemini_response(user_input)
print(f"Bot: {response}")'''


'''
# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"reply": "Please provide a valid input."})

        # Send user input to the Google Gemini chat model
        chat_response = chat_session.send_message(user_input)

        # Extract the chatbot's response
        chatbot_response = chat_response.get('content', "Sorry, I couldn't understand that.")

        return jsonify({"reply": chatbot_response})
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return jsonify({"reply": "Something went wrong. Please try again later."})'''


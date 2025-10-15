import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Initialize Flask App and CORS ---
app = Flask(__name__)
# CORS is needed to allow the frontend (running on a different address)
# to communicate with this backend.
CORS(app)

# --- Configure Google Gemini API ---
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('models/gemini-pro-latest')
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    # Handle the error appropriately, maybe exit or use a fallback
    model = None

# --- In-memory Session Storage ---
# For a real application, you would use a database like Redis, SQLite, or PostgreSQL.
# A simple dictionary is fine for this project.
# The structure will be: { "session_id": {"history": [...]}, ... }
chat_sessions = {}

# --- The Core Prompt for the AI ---
# This prompt is crucial. It sets the rules, provides the data (FAQs),
# and defines the escalation procedure.
SYSTEM_PROMPT = """
You are 'Futura', a friendly and highly advanced AI customer support assistant for a fictional e-commerce store called "Nexus Store".

Your primary goal is to answer customer questions based *only* on the provided Frequently Asked Questions (FAQs). Do not make up information.

**FAQs:**
Q: What are your shipping options?
A: We offer Standard Shipping (5-7 business days), Expedited Shipping (2-3 business days), and Next-Day Shipping.

Q: How can I track my order?
A: Once your order has shipped, you will receive an email with a tracking number and a link to the carrier's website. You can also find tracking information in your account dashboard under "Order History".

Q: What is your return policy?
A: We accept returns within 30 days of purchase. Items must be unused and in their original packaging. To start a return, please visit our returns portal or contact support.

Q: How do I change my password?
A: You can change your password by going to your Account Settings, selecting the "Security" tab, and clicking "Change Password".

Q: Do you ship internationally?
A: Currently, we only ship within the United States and Canada.

**Your Instructions:**
1.  When a user asks a question, find the most relevant answer from the FAQs above.
2.  If the user's question can be answered from the FAQs, provide a clear and concise answer.
3.  If the user's question *cannot* be answered from the FAQs, or if they express clear frustration (e.g., "this is not helpful", "I want to talk to a human"), or ask to speak to a person, you MUST trigger an escalation.
4.  **To trigger an escalation**, respond with the exact phrase starting with 'ESC:': `ESC:I am sorry, but I cannot answer that. I will connect you to a human agent who can better assist you.` The backend system will detect 'ESC:' to start the escalation process.
5.  Maintain a friendly and helpful tone.
6.  Keep the conversation history in mind to understand follow-up questions.
"""

@app.route('/chat', methods=['POST'])
def chat():
    if not model:
        return jsonify({"error": "Gemini API not configured"}), 500
        
    data = request.json
    session_id = data.get('session_id')
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # --- Session Management ---
    if not session_id or session_id not in chat_sessions:
        session_id = str(uuid.uuid4())
        # The history for Gemini needs to be a list of alternating user/model parts
        # We start it with our system prompt to set the context for the AI
        chat_sessions[session_id] = {
            "history": [
                # The Gemini API is more effective when the system instructions are part of the first user turn.
                {'role': 'user', 'parts': [SYSTEM_PROMPT + "\n\nUser Question: " + "Hello!"]},
                {'role': 'model', 'parts': ["Hello! I am Futura, your AI assistant for Nexus Store. How can I help you today?"]}
            ]
        }
    
    # Retrieve the chat history for the current session
    history = chat_sessions[session_id]["history"]
    
    try:
        # Start a chat session with the model using the existing history
        chat_session = model.start_chat(history=history)

        # Send the new user message to the model
        response = chat_session.send_message(user_message)
        bot_response_text = response.text

        # --- Update Session History ---
        # Add the user's message and the bot's response to our stored history
        history.append({'role': 'user', 'parts': [user_message]})
        history.append({'role': 'model', 'parts': [bot_response_text]})
        
        # Handle escalation logic on the backend if needed
        final_response = bot_response_text
        if bot_response_text.startswith('ESC:'):
            print(f"Escalation triggered for session {session_id}.")
            # Here you could add logic to notify a human agent, create a ticket, etc.
            final_response = bot_response_text.replace('ESC:', '').strip()


        return jsonify({
            "response": final_response,
            "session_id": session_id
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
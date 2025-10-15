# AI Customer Support Bot 🤖

**Project By:** Sanjana Sajan Gharat 
**University:** VIT BHOPAL UNIVERSITY 
**Registration Number:** 22BCE11063

This project is a simulation of an advanced AI-powered customer support chatbot. It uses Google's Gemini Pro model to answer frequently asked questions, maintain conversation context, and escalate to a human agent when necessary. The application features a modern, futuristic chat interface and a robust Python Flask backend.


![Demo Video](https://via.placeholder.com/800x450?text=Demo+Video+Placeholder)

---

## Features

- **🧠 Conversational AI:** Utilizes the Google Gemini Pro model for natural and intelligent responses.
- **📚 FAQ-Based Knowledge:** The bot's knowledge is strictly limited to a provided set of FAQs, preventing it from making up information.
- **💾 Contextual Memory:** Maintains a session history, allowing for follow-up questions and a more natural conversation flow.
- **🚨 Escalation Simulation:** Automatically detects when a question is outside its scope or when the user requests a human, and triggers a simulated escalation.
- **⚙️ REST API Backend:** Built with Python and Flask, providing a clean separation between the frontend and the core logic.
- **✨ Futuristic UI:** A responsive and visually appealing chat interface built with modern CSS.

---

## Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **LLM API**: Google Gemini Pro (via `google-generativeai`)
- **Frontend**: HTML, CSS, JavaScript

---

## Project Structure

```
ai-support-bot/
├── .gitignore          # Specifies files for Git to ignore
├── README.md           # This file
├── backend/
│   ├── app.py          # Main Flask application with API logic
│   ├── requirements.txt  # Python dependencies
│   └── .env            # Stores the secret API key
└── frontend/
    ├── index.html      # The chat interface
    └── styles.css      # Styling for the interface
```

---

## Local Setup & Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.8+
- A Google AI Studio API Key. You can get one for free from [aistudio.google.com](https://aistudio.google.com/).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-support-bot.git
cd ai-support-bot
```

### 2. Set Up the Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create and activate a virtual environment:

```bash
# Create the environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Create the environment file to store your API key. Create a new file named `.env` inside the `backend` folder and add your key:

```
GEMINI_API_KEY="YOUR_GOOGLE_AI_STUDIO_API_KEY"
```

**Important:** Do not share this file or commit it to Git. The `.gitignore` file is already set up to prevent this.

### 3. Run the Application

1. **Start the Backend Server:**
   In your terminal (while inside the `backend` directory with the virtual environment activated), run the Flask app:

```bash
python app.py
```

The server will start and listen on `http://127.0.0.1:5000`.

2. **Launch the Frontend:**
   Navigate to the `frontend` folder in your file explorer and open the `index.html` file directly in your web browser (e.g., Chrome, Firefox).

You can now interact with your AI support bot!

---

## How It Works

The application's logic is straightforward:

1. **User Interaction:** The user types a message in the chat interface and hits send.
2. **API Request:** The JavaScript in `index.html` sends a `POST` request to the `/chat` endpoint of the local Flask server. This request includes the user's message and the current `session_id` (if one exists).
3. **Session Management:** The Flask backend (`app.py`) uses a simple dictionary to store chat histories based on the `session_id`. If it's a new user, a new session is created.
4. **LLM Prompting:** The backend retrieves the conversation history and sends it along with the new user message to the Google Gemini API. A detailed system prompt (see below) is included in the first turn to instruct the AI on its persona, rules, and knowledge base.
5. **Escalation Check:** The AI is instructed to prefix its response with `ESC:` if it cannot answer a question. The backend checks for this prefix to simulate an escalation process.
6. **API Response:** The backend receives the response from Gemini, packages it in a JSON object with the `session_id`, and sends it back to the frontend.
7. **Display Response:** The JavaScript dynamically creates a new message bubble and displays the AI's response in the chat window.

---

## LLM Prompting Strategy

The core of the bot's behavior is controlled by a single, comprehensive **system prompt**. This prompt is sent as the very first message in the conversation history to set the context for the Gemini model. It defines the AI's persona, provides the knowledge base (FAQs), and sets the strict rules for answering and escalating.

<details>
<summary>Click to view the full System Prompt</summary>

```
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
```

</details>

---

## Demo Video

[![Demo Video](https://via.placeholder.com/800x450?text=Click+for+Demo+Video)](https://your-demo-video-link.com)

---



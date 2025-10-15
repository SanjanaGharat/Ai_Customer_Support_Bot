# 🤖 AI Support Bot - Backend

This folder contains the core logic and server for the AI Support Bot. It's the "brain" of the operation, responsible for handling user requests, managing conversation sessions, and communicating with the Google Gemini API.

---

## Technologies Used

The backend is built with a lightweight and powerful Python stack, ideal for creating robust APIs.

### **Python**
- **Role:** The primary programming language used for all server-side logic.

### **Flask**
- **Role:** A micro web framework used to create the web server and the REST API. It handles incoming HTTP requests from the frontend and sends back JSON responses.

### **`google-generativeai`**
- **Role:** The official Google Python SDK for the Gemini API. This library simplifies the process of sending prompts and receiving generated content from the language model.

### **`python-dotenv`**
- **Role:** A utility for managing environment variables. It allows us to securely load our secret `GEMINI_API_KEY` from a `.env` file without hardcoding it into our source code.

### **`Flask-Cors`**
- **Role:** A Flask extension for handling Cross-Origin Resource Sharing (CORS). This is necessary because the frontend (running on a `file://` or different web address) needs permission to make requests to our backend server (running on `http://127.0.0.1:5000`).

---

## Files in this Directory

### **`app.py`**
This is the main application file. It contains all the server logic, including:
- Initializing the Flask application
- Configuring the Google Gemini API client
- Implementing in-memory session management to track conversation history
- Defining the crucial **system prompt** that instructs the AI
- Creating the `/chat` API endpoint that receives user messages and returns the AI's response

### **`requirements.txt`**
This file lists all the Python libraries the project depends on. It allows for easy installation of dependencies using the command: `pip install -r requirements.txt`.

### **`.env`**
**🔑 Important:** This file is for storing your secret `GEMINI_API_KEY`. It is **intentionally excluded** from version control by the main `.gitignore` file to protect your credentials. You must create this file yourself.

---

## Setup and Running Instructions

### 1. Navigate to this directory in your terminal:
```bash
cd backend
```

### 2. Create and activate a virtual environment:
This isolates the project's dependencies.
```bash
# Create the environment
python -m venv venv

# Activate it on macOS/Linux
source venv/bin/activate

# Activate it on Windows
.\venv\Scripts\activate
```

### 3. Install the required libraries:
```bash
pip install -r requirements.txt
```

### 4. Create the environment file:
Create a new file named `.env` in this directory and add your API key:
```
GEMINI_API_KEY="your-secret-api-key-goes-here"
```

### 5. Run the Flask server:
```bash
python app.py
```

If successful, you will see output indicating the server is running in debug mode on `http://127.0.0.1:5000`. The server is now ready to accept requests from the frontend.

---

## API Endpoint

The backend exposes a single API endpoint to the frontend.

### **Endpoint:** `POST /chat`

**Description:** Receives a user's message and returns a response from the AI.

**Request Body (JSON):**
```json
{
  "message": "What is your return policy?",
  "session_id": "optional-uuid-string-for-existing-chats"
}
```

**Response Body (JSON):**
```json
{
  "response": "We accept returns within 30 days of purchase...",
  "session_id": "uuid-string-for-this-chat-session"
}
```

**Error Response (JSON):**
```json
{
  "error": "Error message describing what went wrong"
}
```

---

## Key Features

### **Session Management**
- Uses in-memory session storage to maintain conversation history
- Each session is identified by a unique UUID
- Conversation context is preserved across multiple messages

### **AI Prompt Engineering**
- Implements a comprehensive system prompt that defines the AI's persona
- Enforces FAQ-based responses to prevent hallucinations
- Includes escalation triggers for out-of-scope questions

### **Error Handling**
- Comprehensive error handling for API failures
- Graceful degradation when Gemini API is unavailable
- Input validation for user messages

### **Security**
- Environment variable protection for API keys
- CORS configuration for secure cross-origin requests
- Input sanitization and validation

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google AI Studio API key | Yes |
| `FLASK_ENV` | Set to 'development' for debug mode | No |

---

## Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**
   - Solution: Ensure you've activated the virtual environment and run `pip install -r requirements.txt`

2. **API Key Error**
   - Solution: Verify your `.env` file exists in the backend directory and contains a valid `GEMINI_API_KEY`

3. **CORS Errors**
   - Solution: Ensure `Flask-CORS` is installed and the frontend is making requests to the correct backend URL

4. **Port Already in Use**
   - Solution: Change the port in `app.py` or stop other applications using port 5000

---

## Development Notes

- The server runs in debug mode by default for development
- Session data is stored in memory and will be lost on server restart
- For production deployment, consider using a persistent session storage solution
- The system prompt can be modified in `app.py` to change the AI's behavior
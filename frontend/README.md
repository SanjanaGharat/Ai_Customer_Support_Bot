# 🤖 AI Support Bot - Frontend

This folder contains all the files for the user-facing chat interface of the AI Support Bot. It's a self-contained, static frontend designed to be simple, visually appealing, and efficient. It communicates with a separate backend server to get the AI-generated responses.

---

## Technologies Used

This frontend is built with the fundamental technologies of the web, ensuring maximum compatibility and performance without relying on heavy frameworks.

### **HTML (HyperText Markup Language)**
- **Role:** Provides the core structure and content of the chat application.
- **In this project:** `index.html` defines the main elements like the chat container, header, message display area (`div` with id `chat-box`), and the user input form.

### **CSS (Cascading Style Sheets)**
- **Role:** Styles the application, handling everything from layout and colors to animations and responsiveness.
- **In this project:** `styles.css` is responsible for the futuristic aesthetic, including the gradient background, "frosted glass" effect (`backdrop-filter`), custom scrollbar, message bubble styling, and the send button's hover animation.

### **JavaScript (Vanilla JS)**
- **Role:** Provides interactivity and logic, turning the static HTML page into a dynamic application.
- **In this project:** The `<script>` tag in `index.html` contains all the client-side logic. Its key responsibilities are:
  - **Event Handling:** Listening for clicks on the send button and 'Enter' key presses.
  - **DOM Manipulation:** Dynamically creating new message bubbles and adding them to the chatbox.
  - **API Communication:** Using the `fetch` API to send the user's message to the backend server and handle the response.
  - **Session Management:** Storing the `sessionId` returned by the server to maintain conversation context across multiple messages.

---

## File Structure

```
frontend/
├── index.html      # Main HTML file containing the chat interface structure
└── styles.css      # CSS stylesheet for visual design and animations
```

---

## How to Run

1. **First, ensure the backend server is running** (usually on `http://127.0.0.1:5000`). The frontend cannot function without it.
2. **Open the application:** Simply open the `index.html` file in any modern web browser (e.g., Chrome, Firefox, Safari, Edge).
3. **Start chatting:** Type your message in the input field and press Enter or click the send button to interact with the AI bot.

---

## Backend Connection

The frontend communicates with the backend via a single API endpoint. The URL for this endpoint is hardcoded in the `sendMessage` function within the `<script>` tag of `index.html`.

### Local Development Configuration
For local development, the URL is set to:

```javascript
const response = await fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: userMessage, session_id: sessionId })
});
```

### Deployment Configuration
**IMPORTANT:** When you deploy the application to a live hosting service, you **must change this URL** to your live backend's public address. For example:

```javascript
// For production deployment
const response = await fetch('https://your-app-name.onrender.com/chat', {
    // ... rest of the configuration
});
```

---

## Key Features

- **Real-time Chat Interface:** Clean, modern design with smooth message transitions
- **Responsive Design:** Works on both desktop and mobile devices
- **Session Persistence:** Maintains conversation context using session IDs
- **User-Friendly Input:** Supports both button click and Enter key for sending messages
- **Visual Feedback:** Loading indicators and clear message bubbles for user and bot responses

---

## Browser Compatibility

This frontend is compatible with all modern browsers that support:
- ES6+ JavaScript features
- CSS Grid and Flexbox
- Fetch API
- CSS Backdrop Filter (for the frosted glass effect)

---

## Development Notes

- The frontend is designed to be framework-free for simplicity and fast loading
- All JavaScript is contained within the HTML file for easy deployment
- CSS uses modern features but includes fallbacks for broader compatibility
- The design follows a mobile-first approach


# 🤖 AI Chatbot

A sleek, interactive, and theme-toggle-capable AI chatbot web app built with **Flask**, **HTML/CSS/JS**, and **OpenAI API**, featuring:
- 🌗 Light/Dark mode toggle
- 📝 Persistent chat history (JSON-based)
- 📄 Chat export/download
- 🧭 Collapsible sidebar with search, delete, and icon support
- 🔄 Multiple sessions support

---

## 🚀 Features

- **Multi-Chat Support**: Start new chats, switch between them, and retain history.
- **Sidebar**:
  - Collapsible menu with a hamburger icon
  - Search/filter chat titles
  - Add/delete chats with icons
- **Dark Mode**: Easily toggle themes with a top-right switch.
- **Persistent Chat History**: Stored locally using a `chat_data.json` file.
- **Download/Export Chats**: Save any chat to a `.json` file.
- **Smooth UI**: Built with modern aesthetics in mind using Tailwind-style CSS.

---

## 📁 Project Structure

```
ai-chatbot/
│
├── app.py               # Flask backend app
├── chatbot.py           # Chat interaction logic
├── chat_data.json       # Stores persistent chats
├── requirements.txt     # Python dependencies
├── .env                 # API keys and secrets (not tracked)
│
├── templates/
│   └── index.html       # Frontend HTML
│
├── static/
│   └── style.css        # UI styling
│
├── exports/
│   └── ...              # Exported chat histories
```

---

## ⚙️ Setup Instructions

1. **Clone or unzip this repo**  
   ```bash
   git clone <repo_url>
   cd ai-chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**  
   Create a `.env` file and add:
   ```
   OPENAI_API_KEY=your_openai_secret_key
   ```

5. **Run the app**  
   ```bash
   python app.py
   ```

6. Open your browser and go to:  
   ```
   http://127.0.0.1:5000
   ```

---

## 📦 Dependencies

- Flask
- OpenAI
- Python-dotenv
- UUID
- JSON

Install them with:
```bash
pip install flask openai python-dotenv
```

---

## 📸 UI Preview

Include screenshots like these in your actual `README.md`:
- Home page with chatbot and sidebar
- Theme toggle in action
- Chat download/export button
- Collapsible sidebar open/closed

---

## 🔐 Security Notes

- **Never expose your `.env` or `OPENAI_API_KEY`** publicly.
- Add `.env` to your `.gitignore` file to avoid accidental commits.

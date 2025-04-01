# Jarvis Voice Assistant

A web-based voice assistant built with Python Flask and JavaScript that can perform various tasks through voice commands.

## Features

- Voice recognition and text-to-speech
- Command history tracking
- Real-time voice visualization
- Various commands including:
  - Wikipedia searches
  - Opening websites
  - Playing music
  - Time and date information
  - Task management
  - WhatsApp messaging

## Technologies Used

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- Libraries:
  - pyttsx3 for text-to-speech
  - speech_recognition for voice recognition
  - plyer for notifications
  - wikipedia for searches
  - pywhatkit for WhatsApp integration

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. Install the required packages:
```bash
pip install flask pyttsx3 speechrecognition plyer pyautogui wikipedia pywhatkit
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Click the "Start Listening" button
2. Speak a command
3. Wait for Jarvis to process and respond

## Available Commands

- "Hello" - Get a welcome message
- "Play music" - Play random music
- "Say time" - Get current time
- "Say date" - Get current date
- "New task [task]" - Add a new task
- "Speak task" - List all tasks
- "Show work" - Display tasks as notification
- "Open youtube" - Open YouTube
- "Open [application]" - Open specified application
- "Wikipedia [query]" - Search Wikipedia
- "Search google [query]" - Search Google
- "Send whatsapp" - Send WhatsApp message

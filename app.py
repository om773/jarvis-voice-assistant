from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '')
    
    try:
        # Process the command using your existing main_process logic
        response = main_process(command)
        return jsonify({"status": "success", "response": response})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    return audio

def main_process(command):
    # Your existing command processing logic here
    # Modified to return responses instead of speaking directly
    
    command = command.lower()
    
    if "hello" in command:
        return speak("Welcome, How can i help you.")
    elif "play music" in command:
        speak("playing music")
        song = random.randint(1,3)
        if song == 1:
            webbrowser.open("https://www.youtube.com/watch?v=WzQBAc8i73E&pp=ygUUY29weXJpZ2h0IGZyZWUgbXVzaWM%3D")
        elif song == 2:
            webbrowser.open("https://www.youtube.com/watch?v=Vb_3FuiVHBM&pp=ygUUY29weXJpZ2h0IGZyZWUgbXVzaWM%3D")
        elif song == 3:
            webbrowser.open("https://www.youtube.com/watch?v=Jx02XQTz2LU&pp=ygUUY29weXJpZ2h0IGZyZWUgbXVzaWM%3D")
        return "Playing music"
    elif "say time" in command:
        now_time = datetime.datetime.now().strftime("%H:%M")
        return speak("current time is "+str(now_time))
    elif "say date" in command:
        now_time = datetime.datetime.now().strftime("%d:%m")
        return speak("current date is "+str(now_time))
    elif "new task" in command:
        task = command.replace("new task","")
        task = task.strip()
        if task != "":
            speak("Adding task: "+task)
            with open ("todo.txt","a") as file:
                file.write(task + "\n")
            return "Task added"
    elif "speak task" in command:
        with open ("todo.txt","r") as file:
            return speak("work we have to do today is : "+file.read())
    elif "show work" in command:
        with open ("todo.txt","r") as file:
            tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            )
            return "Showing tasks"
    elif "open youtube" in command:
        webbrowser.open("www.youtube.com")
        return "Opening YouTube"
    elif "open" in command:
        query = command.replace("open", "")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(2)
        pyautogui.press("enter")
        return "Opening " + query
    elif "wikipedia" in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        return results
    elif "search google" in command:
        speak('Searching Google...')
        command = command.replace("search google", "")
        webbrowser.open("https://www.google.com/search?q="+command)
        return "Searching Google"
    elif "send whatsapp" in command:
        pwk.sendwhatmsg("+918141838719", "Hi,How are you ", 11, 8,40)
        return "Sending WhatsApp message"
    else:
        return "I didn't understand that command"

if __name__ == "__main__":
    app.run(debug=True)
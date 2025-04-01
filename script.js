class VoiceAssistant {
    constructor() {
        this.recognition = null;
        this.synthesis = window.speechSynthesis;
        this.isListening = false;
        this.visualizer = null;
        
        this.initializeElements();
        this.setupSpeechRecognition();
        this.setupVisualizer();
        this.addEventListeners();
    }

    initializeElements() {
        this.startButton = document.getElementById('startButton');
        this.statusText = document.getElementById('status-text');
        this.historyDiv = document.getElementById('history');
        this.visualizerCanvas = document.getElementById('visualizer');
    }

    setupSpeechRecognition() {
        if ('webkitSpeechRecognition' in window) {
            this.recognition = new webkitSpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'en-US';

            this.recognition.onstart = () => {
                this.isListening = true;
                this.updateStatus('Listening...');
            };

            this.recognition.onresult = (event) => {
                const command = event.results[0][0].transcript;
                this.updateStatus('Processing: ' + command);
                this.processCommand(command);
            };

            this.recognition.onerror = (event) => {
                this.updateStatus('Error: ' + event.error);
                this.isListening = false;
            };

            this.recognition.onend = () => {
                this.isListening = false;
                this.updateStatus('Stopped listening');
            };
        }
    }

    async processCommand(command) {
        try {
            const response = await fetch('/process_command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command: command })
            });

            const data = await response.json();
            
            if (data.status === 'success') {
                this.updateHistory(command, data.response);
            } else {
                this.updateHistory(command, 'Error: ' + data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            this.updateHistory(command, 'Error processing command');
        }
    }

    updateStatus(message) {
        if (this.statusText) {
            this.statusText.textContent = message;
        }
    }

    updateHistory(command, response) {
        if (this.historyDiv) {
            const entry = document.createElement('div');
            entry.className = 'history-entry';
            entry.innerHTML = `
                <div class="command">You: ${command}</div>
                <div class="response">Jarvis: ${response}</div>
            `;
            this.historyDiv.appendChild(entry);
            this.historyDiv.scrollTop = this.historyDiv.scrollHeight;
        }
    }

    setupVisualizer() {
        // Add visualization logic here if needed
    }

    addEventListeners() {
        if (this.startButton) {
            this.startButton.addEventListener('click', () => {
                if (!this.isListening) {
                    this.recognition.start();
                } else {
                    this.recognition.stop();
                }
            });
        }
    }
}

// Initialize the voice assistant when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const assistant = new VoiceAssistant();
});
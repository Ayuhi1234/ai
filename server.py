from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/start-chatbot')
def start_chatbot():
    try:
        chatbot_path = os.path.abspath("D:/BAsiliya/Untitled/Untitled/application/CHATBOT/gui.py")  # Ensure correct path
        subprocess.Popen(["python", chatbot_path])  # Run Python GUI file
        return "Chatbot launched!", 200
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
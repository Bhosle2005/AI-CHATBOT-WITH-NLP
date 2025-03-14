from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined chatbot responses
responses = {
   "hello": "Hi! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm your friendly chatbot!",
    "ohh great": "yess thank you!!",
    "what can you do": "I can answer your questions and chat with you. How can I help?",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
    "what is flask": "Flask is a lightweight web framework for Python.",
    "who created you": "I was created by a programmer to assist you!",
    "what is python": "Python is a popular programming language known for its simplicity and readability.",
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    print(f"User message: {user_message}")  # Debugging
    bot_response = get_response(user_message)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)


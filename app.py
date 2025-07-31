from flask import Flask, request, jsonify
from modules.chatbot import respond

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Ahoj! API běží. Pošli POST na /chat."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    
    if not user_input:
        return jsonify({"error": "Zpráva chybí!"}), 400

    reply = respond(user_input)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)

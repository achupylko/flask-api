from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()
    print("Отримано:", data)

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "Всі поля обов'язкові"}), 400
    
    return jsonify({"message": "Повідомлення отримано!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import os


def create_app(message=None):
    flask_app = Flask(__name__)
    response_message = message if message is not None else os.getenv("MSG", "Hello DevOps!")

    @flask_app.route("/")
    def home():
        return jsonify({"message": response_message})

    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
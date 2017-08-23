import os
from flask import Flask

from controllers import Controller
controller = Controller()

app = Flask(__name__)


@app.route("/recognize.json", methods=["POST"])
def recognize_json():
    return controller.recognize_json()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

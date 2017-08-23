import os
import sys
import flask


class Controller():
    def __init__(self, nn):
        self.nn = nn

    def recognize_json(self):
        return flask.jsonify({"digit": "-1/12"})


def set_nn(nn):
    self = sys.modules[__name__]
    self.nn = nn
    self.controller = Controller(nn)


app = flask.Flask(__name__)


@app.route("/recognize.json", methods=["POST"])
def recognize_json():
    return controller.recognize_json()


if __name__ == "__main__":
    from digit_recognizor import create_trained_nn
    nn = create_trained_nn()
    set_nn(nn)

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

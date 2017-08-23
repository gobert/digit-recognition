import os
import sys

import flask
import numpy as np
from scipy import ndimage


class InputError(Exception):
    pass


class Controller():
    def __init__(self, nn):
        self.nn = nn

    def recognize_json(self):
        try:
            image = np.array([self.__image__()]).reshape(28, 28, 1)
            recognized = self.nn.predict(image)

            return flask.jsonify({"digit": recognized})
        except InputError as e:
            return flask.jsonify({"Error": "No image found"}), 400
        except IOError as e:
            return flask.jsonify({"Error": "Image can not be read"}), 400

    def __image__(self):
        imagefile = flask.request.files.get("image", None)
        if not imagefile:
            raise InputError("No image detected")
        else:
            return ndimage.imread(imagefile, flatten=True)


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

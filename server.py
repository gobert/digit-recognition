import os
import sys

import flask
from raven.contrib.flask import Sentry

import numpy as np
from scipy import ndimage

app = flask.Flask(__name__)
sentry_uri = os.environ.get("SENTRY_URI", "")
sentry = Sentry(app, dsn=sentry_uri)


class InputError(Exception):
    pass


class Controller():
    def __init__(self, nn):
        self.nn = nn

    def debug_error():
        raise Exception("Dummy exception to test error logging on SEntry")

    def recognize_json(self):
        try:
            recognized = self.nn.predict(self.__image__())

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


@app.route("/_debug/error")
def debug_error():
    return controller.debug_error()


@app.route("/recognize.json", methods=["POST"])
def recognize_json():
    return controller.recognize_json()


if __name__ == "__main__":
    from digit_recognizor import create_trained_nn
    nn = create_trained_nn()
    set_nn(nn)

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

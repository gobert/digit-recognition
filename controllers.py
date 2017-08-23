import flask


class Controller():
    def recognize_json(self):
        return flask.jsonify({"digit": "-1/12"})

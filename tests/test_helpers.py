from flask_testing import TestCase


# import files of parent directoy
def import_app():
    from inspect import getsourcefile
    import os.path
    import sys
    current_path = os.path.abspath(getsourcefile(lambda: 0))
    current_dir = os.path.dirname(current_path)
    sys.path.append(current_dir + "/..")

    from server import app
    return app


class MyTest(TestCase):
    def create_app(self):
        # import app
        app = import_app()
        app.config["TESTING"] = True

        return app

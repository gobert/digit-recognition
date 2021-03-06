from flask_testing import TestCase
import unittest

from scipy import ndimage
import numpy as np

# import files of parent directoy
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
sys.path.append(current_dir + "/..")
from server import app, set_nn


app.config["TESTING"] = True
# create trained NN
from digit_recognizor import create_trained_nn
nn = create_trained_nn()
set_nn(nn)


class MyTest(TestCase):
    def create_app(self):
        return app


class ShowRecogitionJSON(MyTest):
    def test_with_correct_image(self):
        image = open("./tests/fixtures/1a_.png")
        response = self.client.post("/recognize.json",
                                    data={"image": image})
        self.assertEquals(response.status, "200 OK")
        self.assertEquals(response.json, {"digit": 1})

    def test_with_incorrect_image(self):
        image = open("./tests/fixtures/corrupted.png")
        response = self.client.post("/recognize.json",
                                    data={"image": image})
        self.assertEquals(response.status, "400 BAD REQUEST")

    def test_with_big_images(self):
        image = open("./tests/fixtures/big.JPG")
        response = self.client.post("/recognize.json",
                                    data={"image": image})
        self.assertEquals(response.status, "200 OK")

    def test_without_image(self):
        response = self.client.post("/recognize.json")
        self.assertEquals(response.status, "400 BAD REQUEST")


class DigitPredictor(MyTest):
    def test_image_recognition(self):
        # get image in good format
        imagefile = "./tests/fixtures/1a_.png"
        image = ndimage.imread(imagefile, flatten=True)

        self.assertEquals(nn.predict(image), 1)


if __name__ == "__main__":
    unittest.main()

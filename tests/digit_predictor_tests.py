import unittest
from scipy import ndimage
import numpy as np

from test_helpers import MyTest


class DigitPredictor(MyTest):
    def test_image_recognition(self):
        # create trained NN
        from digit_predictor import train_nn
        self.nn = train_nn()

        # get image in good format
        imagefile = "./tests/fixtures/1a_.png"
        image = ndimage.imread(imagefile, flatten=True)
        image = np.array([image]).reshape(28, 28, 1)

        self.assertEquals(self.nn.predict(image), 1)


if __name__ == "__main__":
    unittest.main()

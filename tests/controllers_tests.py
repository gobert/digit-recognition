from test_helpers import MyTest
import unittest


class ShowRecogitionJSON(MyTest):
    def test_without_image(self):
        response = self.client.post("/recognize.json")
        self.assertEquals(response.status, "200 OK")


if __name__ == "__main__":
    unittest.main()

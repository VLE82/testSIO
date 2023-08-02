import unittest
import sys
sys.path.append("..")

from helloworld import hello_world

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello, World!")

if __name__ == "__main__":
    unittest.main()


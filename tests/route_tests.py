#!flask/bin/python
import os
import unittest

from FlaskHello import hello


class TestCase(unittest.TestCase):
    def setUp(self):
        pass
#        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_hello_world(self):
        expected = "Hello World"
        recieved = hello.hello()

        assert expected == recieved

    def test_hello_name(self):
        expected = "Hello Weyland"
        recieved = hello.hello_name("Weyland")
        assert expected == recieved

if __name__ == '__main__':
    unittest.main()

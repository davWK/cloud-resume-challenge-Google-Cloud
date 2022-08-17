#!/usr/bin/env python3
import json

from main import getCount
import requests
import unittest


class testgetCount(unittest.TestCase):
    def do_test(self):
        self.assertTrue(type(getCount()) is dict)

    def test_get_visitor_number_response_is_dict(self):
        response = requests.get("https://us-central1-alilikpo-228.cloudfunctions.net/get_visitor_number")
        data = json.loads(response.content)
        self.assertIs(type(data), dict)
        self.assertIn('count', data)


if __name__ == '__main__':
    unittest.main()

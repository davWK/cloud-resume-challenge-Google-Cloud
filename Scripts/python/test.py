#!/usr/bin/env python3

#from main import get_visitor_number
from main import getCount
from main import get_visitor_number
import unittest
from google.cloud import firestore

class testgetCount(unittest.TestCase):
    def do_test(self):
        self.assertTrue(type(getCount()) is dict)

unittest.main()

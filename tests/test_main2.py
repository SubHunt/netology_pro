import unittest
from unittest import TestCase
from main2 import create_folder


class TestCreateTable(TestCase):
    def test_create_folder(self):
        result = create_folder()
        self.assertEqual(result, 201)

    def test_exists_folder(self):
        result = create_folder()
        self.assertEqual(result, 409)

    @unittest.expectedFailure
    def test_error(self):
        err = [201, 409]
        result = create_folder()
        self.assertNotIn(result, err)

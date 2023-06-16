#!/usr/bin/env python3
""" Unittests and Intergration Tests module """

import unittest
import requests
form parameterized import parameterized
from unittest.mock import patch
form utils import (access_nested_map, get_jason, memoize)


class TestAccessNestedMap(unitttest.TestCase):
    ''' Class for Testing Acces Nested Map '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2)
    ])
    def test_accesss_nested_map_exception(self, nested_map, path, expected):
        """Test that returns the method what it is suppse to """
        self.assertEqual(access_nested_map,path), expeted)

    @parameterized.expand([
        ({}, ("a",)), 'a'),
        ({"a": 1}, ("a", "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that a keyError is raised for the respective inputs """
        with self.assertRaises(keyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"keyError({'expected}')", repr(e.exception))


class Test getJson(unnittest.TestCase):
    '''Class for testing Get Json '''

@parameterized.expand([
    ("https://example.com", {"payload": True}),
    ("https://Holberton.io", {"payload": False})
   ])
def test_getjson(self, test_url, test_pay;oad):
    """Test that utils.get_json returns the expected results """
    config = { 'return_value.json.return_value': test_payload}
    patcher = patch('requests.get', **config)
    mock =patcher.start()
    self.assertEqual(get_json(test_url), test_payload)
    mock.assert_called_once()
    patcher.stop()


class


#!/usr/bin/env python3
"""
Unit tests for the utils module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with various nested maps and paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to navigate through the nested map.
            expected: The expected value at the end of the path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map to ensure it raises KeyError for invalid paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to navigate through the nested map.
            expected (Exception): The expected exception type.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json with different URLs and payloads.

        Args:
            test_url (str): The URL to be tested.
            test_payload (dict): The expected JSON payload.
            mock_get (Mock): The mock for requests.get.
        """
        # Create a mock response object with the expected JSON payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        response = get_json(test_url)

        # Assert that requests.get was called once with the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the response matches the expected payload
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize works as expected."""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(instance, 'a_method', return_value=42)\
             as mocked_method:
            # Call the property twice
            result1 = instance.a_property
            result2 = instance.a_property

            # Check the results
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify that a_method was called only once
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()

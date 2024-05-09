#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import MagicMock, patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Parameterized unit test"""
    @parameterized.expand(
    [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, output) -> None:
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), output)

if __name__ == "__main__":
    unittest.main()

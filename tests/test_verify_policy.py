import unittest
from unittest.mock import patch
import pytest
from src.verify_policy import RolePolicyParser
from .mock_variables import json_false, json_true


class TestRolePolicyParser(unittest.TestCase):
    """
    Test class for testing the RolePolicyParser class
    """

    def setUp(self):
        """
        Initialize variables for tests
        """
        self.loc_false = "./tests/test_files/IAM_Role_Policy_false.json"
        self.loc_true = "./tests/test_files/IAM_Role_Policy_true.json"
        self.fake_loc = "./AM_Role_Policy.json"
        self.mock_json_false = json_false
        self.mock_json_true = json_true

    def test_parser_instance(self):
        """
        Test of creating an instance of RolePolicyParser
        """
        parser = RolePolicyParser(self.loc_false)
        assert isinstance(parser, RolePolicyParser)

    def test_load_wrong_loc(self):
        """
        Test for raise exceptions when loading a non-existent file
        """
        parser = RolePolicyParser(self.fake_loc)
        with pytest.raises(FileNotFoundError):
            parser.load()

    def test_load(self):
        """
        Check the type correctness of the return in the load method
        """
        parser = RolePolicyParser(self.loc_false)
        assert isinstance(parser.load(), dict)

    def test_verify_json_true(self):
        """
        Tests correctness of verify() return for existing JSON_true
        """
        parser = RolePolicyParser(self.loc_true)
        result = parser.verify()
        self.assertTrue(result)

    def test_verify_json_false(self):
        """
        Tests correctness of verify() return for existing JSON_false
        """
        parser = RolePolicyParser(self.loc_false)
        result = parser.verify()
        self.assertFalse(result)

    @patch.object(RolePolicyParser, "load")
    def test_verify_mock_json_false(self, mock_load):
        """
        Tests correctness of verify() return for mocked JSON_false
        """
        mock_load.return_value = self.mock_json_false
        parser = RolePolicyParser(self.fake_loc)
        result = parser.verify()
        self.assertFalse(result)

    @patch.object(RolePolicyParser, "load")
    def test_verify_mock_json_true(self, mock_load):
        """
        Tests correctness of verify() return for mocked JSON_true
        """
        mock_load.return_value = self.mock_json_true
        parser = RolePolicyParser(self.fake_loc)
        result = parser.verify()
        self.assertTrue(result)

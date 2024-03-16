#!/usr/bin/env python

import os
import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.command = HBNBCommand()

    @patch('sys.stdout', new_callable=MagicMock)
    def test_create_state(self, mock_stdout):
        self.command.do_create("State name=\"California\"")
        self.command.do_create("State name=\"Arizona\"")
        self.command.do_create("all State")
        expected_output = "[[State] ({}) {{'id': '{}', 'created_at': {}, 'updated_at': {}, 'name': 'California'}},".format(
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__()
        )
        expected_output += " [State] ({}) {{'id': '{}', 'created_at': {}, 'updated_at': {}, 'name': 'Arizona'}}]".format(
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__()
        )
        mock_stdout.assert_called_with(expected_output)

    @patch('sys.stdout', new_callable=MagicMock)
    def test_create_place(self, mock_stdout):
        self.command.do_create("Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        self.command.do_create("all Place")
        expected_output = "[[Place] ({}) {{'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '{}', 'max_guest': 10, 'number_rooms': 4, 'updated_at': {}, 'created_at': {}}}]".format(
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__(),
            MagicMock().__str__()
        )
        mock_stdout.assert_called_with(expected_output)

if __name__ == "__main__":
    unittest.main()


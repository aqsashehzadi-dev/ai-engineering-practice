import unittest
import requests
from unittest.mock import Mock, patch

from src.api_client import fetch_user, validate_user


class TestAPIClient(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_fetch_user_success(self, mock_get):
        mock_response = Mock()

        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "name": "Leanne Graham",
            "email": "Sincere@april.biz"
        }

        mock_get.return_value = mock_response

        result = fetch_user(1)

        self.assertEqual(result["name"], "Leanne Graham")
        self.assertEqual(result["email"], "Sincere@april.biz")

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=10
        )

        mock_response.raise_for_status.assert_called_once()
        
    @patch("src.api_client.requests.get")
    def test_fetch_user_http_error(self, mock_get):
        import requests

        mock_response = Mock()

        mock_response.raise_for_status.side_effect = (
            requests.HTTPError("404 Not Found")
        )

        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            fetch_user(999)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/999",
            timeout=10
        )

        mock_response.raise_for_status.assert_called_once()


    @patch("src.api_client.requests.get")
    def test_fetch_user_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout(
            "Request timed out"
        )

        with self.assertRaises(requests.Timeout):
            fetch_user(1)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=10
        )


    @patch("src.api_client.requests.get")
    def test_fetch_user_connection_error(self, mock_get):
        mock_get.side_effect = requests.ConnectionError(
            "Connection failed"
        )

        with self.assertRaises(requests.ConnectionError):
            fetch_user(1)

        mock_get.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=10
        )

    def test_validate_user_success(self):
        user = {
            "name": "Aqsa",
            "email": "aqsa@example.com"
        }

        result = validate_user(user)

        self.assertEqual(result, user)
        self.assertEqual(result["name"], "Aqsa")


    def test_validate_user_missing_email(self):
        user = {
            "name": "Aqsa"
        }

        with self.assertRaisesRegex(
            ValueError,
            "Missing required field: email"
        ):
            validate_user(user)


    def test_validate_user_invalid_email_type(self):
        user = {
            "name": "Aqsa",
            "email": 12345
        }

        with self.assertRaisesRegex(
            ValueError,
            "email must be a string"
        ):
            validate_user(user)


    def test_validate_user_empty_email(self):
        user = {
            "name": "Aqsa",
            "email": "   "
        }

        with self.assertRaisesRegex(
            ValueError,
            "email cannot be empty"
        ):
            validate_user(user)

if __name__ == "__main__":
    unittest.main()
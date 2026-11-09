import requests


def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def validate_user(user):
    if not isinstance(user, dict):
        raise ValueError("API response must be a dictionary.")

    for field in ("name", "email"):
        if field not in user:
            raise ValueError(f"Missing required field: {field}")

        if not isinstance(user[field], str):
            raise ValueError(f"{field} must be a string.")

        if not user[field].strip():
            raise ValueError(f"{field} cannot be empty.")

    return user


if __name__ == "__main__":
    try:
        user = fetch_user(1)
        validated_user = validate_user(user)

        print("Name:", validated_user["name"])
        print("Email:", validated_user["email"])

    except requests.Timeout:
        print("API request timed out.")

    except requests.ConnectionError:
        print("Network connection failed.")

    except requests.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.RequestException as error:
        print(f"API request failed: {error}")

    except ValueError as error:
        print(f"Invalid API response: {error}")
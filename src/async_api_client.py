import asyncio
import httpx

try:
    from .api_client import validate_user
except ImportError:
    from api_client import validate_user


async def fetch_user_async(user_id, client, semaphore):
    """Fetch and validate a user asynchronously."""

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    async with semaphore:
        response = await client.get(url)
        response.raise_for_status()

    return validate_user(response.json())


async def main():
    try:
        semaphore = asyncio.Semaphore(2)

        async with httpx.AsyncClient(timeout=10.0) as client:
            users = await asyncio.gather(
                fetch_user_async(1, client, semaphore),
                fetch_user_async(2, client, semaphore),
                fetch_user_async(3, client, semaphore)
            )

        for user in users:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("-" * 30)

    except httpx.TimeoutException:
        print("API request timed out.")

    except httpx.HTTPStatusError as error:
        print(f"HTTP error: {error}")

    except httpx.RequestError as error:
        print(f"Network request failed: {error}")

    except ValueError as error:
        print(f"Invalid API response: {error}")


if __name__ == "__main__":
    asyncio.run(main())
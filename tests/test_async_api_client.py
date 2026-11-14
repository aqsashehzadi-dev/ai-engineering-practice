import asyncio
import unittest
from unittest.mock import AsyncMock, Mock

import httpx

from src.async_api_client import fetch_user_async


class TestAsyncAPIClient(unittest.IsolatedAsyncioTestCase):

    async def test_fetch_user_success(self):
        response = Mock()
        response.json.return_value = {
            "name": "Test User",
            "email": "test@example.com"
        }

        client = Mock()
        client.get = AsyncMock(return_value=response)

        semaphore = asyncio.Semaphore(2)

        user = await fetch_user_async(
            1, client, semaphore
        )

        self.assertEqual(user["name"], "Test User")
        self.assertEqual(user["email"], "test@example.com")
        client.get.assert_awaited_once_with(
            "https://jsonplaceholder.typicode.com/users/1"
        )
        response.raise_for_status.assert_called_once()

    async def test_fetch_user_invalid_data(self):
        response = Mock()
        response.json.return_value = {
            "name": "Test User"
        }

        client = Mock()
        client.get = AsyncMock(return_value=response)

        semaphore = asyncio.Semaphore(2)

        with self.assertRaises(ValueError):
            await fetch_user_async(
                1, client, semaphore
            )

    async def test_fetch_user_timeout(self):
        client = Mock()
        client.get = AsyncMock(
            side_effect=httpx.ReadTimeout(
                "Request timed out"
            )
        )

        semaphore = asyncio.Semaphore(2)

        with self.assertRaises(httpx.TimeoutException):
            await fetch_user_async(
                1, client, semaphore
            )


    async def test_fetch_user_http_error(self):
        request = httpx.Request(
            "GET",
            "https://jsonplaceholder.typicode.com/users/999"
        )

        response = httpx.Response(
            status_code=404,
            request=request
        )

        client = Mock()
        client.get = AsyncMock(return_value=response)

        semaphore = asyncio.Semaphore(2)

        with self.assertRaises(httpx.HTTPStatusError):
            await fetch_user_async(
                999, client, semaphore
            )

        client.get.assert_awaited_once()


    async def test_fetch_user_cancellation(self):
        request_started = asyncio.Event()

        async def slow_request(url):
            request_started.set()
            await asyncio.sleep(10)

        client = Mock()
        client.get = AsyncMock(side_effect=slow_request)

        semaphore = asyncio.Semaphore(2)

        task = asyncio.create_task(
            fetch_user_async(1, client, semaphore)
        )

        await asyncio.wait_for(
            request_started.wait(),
            timeout=2
        )

        task.cancel()

        with self.assertRaises(asyncio.CancelledError):
            await task

        self.assertTrue(task.cancelled())


    async def test_concurrency_limit(self):
        active_requests = 0
        max_active_requests = 0

        async def mock_get(url):
            nonlocal active_requests, max_active_requests

            active_requests += 1
            max_active_requests = max(
                max_active_requests,
                active_requests
            )

            try:
                await asyncio.sleep(0.05)

                response = Mock()
                response.json.return_value = {
                    "name": "Test User",
                    "email": "test@example.com"
                }
                return response
            finally:
                active_requests -= 1

        client = Mock()
        client.get = AsyncMock(side_effect=mock_get)

        semaphore = asyncio.Semaphore(2)

        users = await asyncio.gather(
            *(
                fetch_user_async(i, client, semaphore)
                for i in range(1, 6)
            )
        )

        self.assertEqual(len(users), 5)
        self.assertEqual(max_active_requests, 2)
        self.assertEqual(active_requests, 0)
        self.assertEqual(client.get.await_count, 5)
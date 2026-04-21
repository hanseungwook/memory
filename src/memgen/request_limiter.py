from __future__ import annotations

import asyncio
import threading
from contextlib import asynccontextmanager, contextmanager


class RequestLimiter:
    """Share one shard-local request budget across async and sync callers."""

    def __init__(self, max_requests: int):
        if max_requests < 1:
            raise ValueError("max_requests must be at least 1")
        self.max_requests = max_requests
        self._semaphore = threading.BoundedSemaphore(max_requests)

    @asynccontextmanager
    async def async_slot(self):
        await asyncio.to_thread(self._semaphore.acquire)
        try:
            yield
        finally:
            self._semaphore.release()

    @contextmanager
    def sync_slot(self):
        self._semaphore.acquire()
        try:
            yield
        finally:
            self._semaphore.release()

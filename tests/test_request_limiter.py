from __future__ import annotations

import asyncio
import threading

import pytest

from memgen.request_limiter import RequestLimiter


@pytest.mark.asyncio
async def test_request_limiter_shares_budget_between_sync_and_async_callers():
    limiter = RequestLimiter(1)
    acquired_async = False
    entered_sync = threading.Event()
    release_sync = threading.Event()

    def hold_sync_slot():
        with limiter.sync_slot():
            entered_sync.set()
            release_sync.wait(timeout=1)

    thread = threading.Thread(target=hold_sync_slot)
    thread.start()

    assert entered_sync.wait(timeout=1)

    async def wait_for_async_slot():
        nonlocal acquired_async
        async with limiter.async_slot():
            acquired_async = True

    task = asyncio.create_task(wait_for_async_slot())
    await asyncio.sleep(0.05)

    assert acquired_async is False
    assert task.done() is False

    release_sync.set()
    await asyncio.wait_for(task, timeout=1)
    thread.join(timeout=1)

    assert acquired_async is True

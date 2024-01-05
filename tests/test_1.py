import asyncio
import time

from async_iterator import aiter, siter

inputs = [1, 2, 3]


def add_1(x: int) -> int:
    return x + 1


async def afunc(it: int) -> int:
    await asyncio.sleep(2)
    return add_1(it)


def sfunc(it: int) -> int:
    time.sleep(2)
    return add_1(it)


def test_aiter():
    async def func():
        result = await aiter(afunc)(inputs)
        return result

    start_time = time.time()
    result = asyncio.run(func())
    end_time = time.time()

    assert result == list(map(add_1, inputs))

    run_time = end_time - start_time
    assert run_time > 1.9
    assert run_time < 2.1


def test_siter():
    def func():
        return siter(sfunc)(inputs)

    start_time = time.time()
    result = func()
    end_time = time.time()

    assert result == list(map(add_1, inputs))

    run_time = end_time - start_time
    assert run_time > 5.9
    assert run_time < 6.1

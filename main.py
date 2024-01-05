import asyncio
import time

from async_iterator import aiter, siter

inputs = [1, 2, 3]


async def afunc(it: int) -> int:
    await asyncio.sleep(2)
    return it + 1


def sfunc(it: int) -> int:
    time.sleep(2)
    return it + 1


async def amain():
    return await aiter(afunc)(inputs)


def smain():
    return siter(sfunc)(inputs)


if __name__ == "__main__":
    format = "%Y-%m-%d %H:%M:%S"

    print(time.strftime(format))
    print("async", asyncio.run(amain()))  # it takes ~2 seconds
    print(time.strftime(format))
    print("sync", smain())  # it takes ~6 seconds
    print(time.strftime(format))

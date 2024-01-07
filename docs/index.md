# async-iterator

<p align="center">
    <em>Easy way to use async iterator without take care about asyncio’s taskgroup.</em>
</p>

---

**Documentation**: <a href="https://async-iterator.lpthong90.dev" target="_blank">https://async-iterator.lpthong90.dev</a>

**Source  Code**: <a href="https://github.com/lpthong90/async-iterator" target="_blank">https://github.com/lpthong90/async-iterator</a>

---

The package helps to use async iterator without take care about asyncio's taskgroup.

## Installation
<div class="termy">

```console
$ pip install async-iterator
---> 100%
Successfully installed async-iterator
```

</div>

## Basic Usage

```Python
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

```

Output
```
2024-01-06 00:58:54
async [2, 3, 4]
2024-01-06 00:58:56
sync [2, 3, 4]
2024-01-06 00:59:02
```






## License

This project is licensed under the terms of the [MIT license](https://github.com/lpthong90/async-iterator/blob/main/LICENSE).
# async-iterator

<p align="center">
    <em>Cách đơn giản để sử dụng async iterator mà không cần quan tâm về TaskGroup của asyncio.</em>
</p>

<p align="center">
    <a href="https://github.com/lpthong90/async-iterator/actions?query=workflow%3ATest" target="_blank">
        <img src="https://github.com/lpthong90/async-iterator/workflows/Test/badge.svg" alt="Test">
    </a>
    <a href="https://github.com/lpthong90/async-iterator/actions?query=workflow%3APublish" target="_blank">
        <img src="https://github.com/lpthong90/async-iterator/workflows/Publish/badge.svg" alt="Publish">
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/lpthong90/async-iterator" target="_blank">
        <img src="https://coverage-badge.samuelcolvin.workers.dev/lpthong90/async-iterator.svg" alt="Coverage">
    <a href="https://pypi.org/project/async-iterator" target="_blank">
        <img src="https://img.shields.io/pypi/v/async-iterator?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pypi.org/project/async-iterator" target="_blank">
        <img alt="Downloads" src="https://img.shields.io/pypi/dm/async-iterator?color=%2334D058" />
    </a>
</p>
<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/async-iterator">
</p>


---

**Tài Liệu**: <a href="https://async-iterator.lpthong90.dev" target="_blank">https://async-iterator.lpthong90.dev</a>

**Mã Nguồn**: <a href="https://github.com/lpthong90/async-iterator" target="_blank">https://github.com/lpthong90/async-iterator</a>

---

Thư viện giúp cho việc sử dụng async iterator mà không cần quan tâm về TaskGroup của asyncio.

## Cài Đặt
<div class="termy">

```console
$ pip install async-iterator
---> 100%
Successfully installed async-iterator
```

</div>

## Cách Dùng

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

Kết quả
```
2024-01-06 00:58:54
async [2, 3, 4]
2024-01-06 00:58:56
sync [2, 3, 4]
2024-01-06 00:59:02
```






## License

Dự án được cấp license là [MIT license](https://github.com/lpthong90/async-iterator/blob/main/LICENSE).
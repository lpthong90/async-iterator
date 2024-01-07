import functools
from typing import Awaitable, Callable, Sequence, TypeVar

import anyio

T_PARAM = TypeVar("T_PARAM")
T_RETURN = TypeVar("T_RETURN")
T = TypeVar("T")


def aiter(
    _func: Callable[[T_PARAM], Awaitable[T_RETURN]],
) -> Callable[[Sequence[T_PARAM]], Awaitable[Sequence[T_RETURN]]]:
    @functools.wraps(_func)
    async def wrapper(iterator: Sequence[T_PARAM]) -> Sequence[T_RETURN]:
        _results = []
        async with anyio.create_task_group() as tg:
            for it in iterator:

                async def get_result_soon(it):
                    _results.append(await _func(it))

                tg.start_soon(get_result_soon, it)
        return _results

    return wrapper


def siter(
    _func: Callable[[T_PARAM], T_RETURN],
) -> Callable[[Sequence[T_PARAM]], Sequence[T_RETURN]]:
    @functools.wraps(_func)
    def wrapper(iterator: Sequence[T_PARAM]) -> Sequence[T_RETURN]:
        _results = [_func(it) for it in iterator]
        return _results

    return wrapper

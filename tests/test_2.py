import asyncio
import time
from typing import Any, Tuple, TypeVar

from sqlalchemy import (
    Column,
    Integer,
    Row,
    Select,
    Sequence,
    String,
    create_engine,
    select,
)

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base

from async_iterator import aiter, siter

TP = TypeVar("TP", bound=Tuple[Any, ...])

engine = create_engine("sqlite:///db.sqlite", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


Base.metadata.create_all(engine)

session = Session(engine)
for table in reversed(Base.metadata.sorted_tables):
    session.execute(table.delete())
session.commit()

users_data = [
    User(name="John Doe", age=25),
    User(name="Jane Doe", age=30),
    User(name="Bob Smith", age=22),
]

session = Session(engine)
session.add_all(users_data)
session.commit()


queries = [select(User), select(User), select(User)]


async def afunc(query: Select) -> Sequence[Row[TP]]:
    with Session(engine) as session:
        await asyncio.sleep(2)
        return session.execute(query).all()


def sfunc(query: Select) -> Sequence[Row[TP]]:
    with Session(engine) as session:
        time.sleep(2)
        return session.execute(query).all()


def test_aiter():
    async def func():
        return await aiter(afunc)(queries)

    start_time = time.time()
    results = asyncio.run(func())
    end_time = time.time()

    for result in results:
        assert len(result) == len(users_data)

    run_time = end_time - start_time
    assert run_time > 1.9
    assert run_time < 2.1


def test_siter():
    def func():
        return siter(sfunc)(queries)

    start_time = time.time()
    results = func()
    end_time = time.time()

    for result in results:
        assert len(result) == len(users_data)

    run_time = end_time - start_time
    assert run_time > 5.9
    assert run_time < 6.1

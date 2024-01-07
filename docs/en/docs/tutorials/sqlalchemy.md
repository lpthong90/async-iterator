# Using with SQLAlchemy

```Python
import asyncio
import logging
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
from sqlalchemy.orm import Session, declarative_base

from async_iterator import aiter, siter

TP = TypeVar("TP", bound=Tuple[Any, ...])

logging.disable(logging.WARNING)

# Create an SQLite in-memory database engine
engine = create_engine("sqlite:///db.sqlite", echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()


# Define a simple model class
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# Create the table
Base.metadata.create_all(engine)

# Remove old data
session = Session(engine)
for table in reversed(Base.metadata.sorted_tables):
    session.execute(table.delete())
session.commit()

# Init data
session = Session(engine)
session.add_all(
    [
        User(name="John Doe", age=25),
        User(name="Jane Doe", age=30),
        User(name="Bob Smith", age=22),
    ]
)
session.commit()

# We need to run execute query multiple times
query = select(User)
queries = [select(User), select(User), select(User)]


# We can execute query with asynchronous method, we assume it takes over 2 seconds for each query
async def afunc(query: Select) -> Sequence[Row[TP]]:
    with Session(engine) as session:
        await asyncio.sleep(2)
        return session.execute(query).all()


# We can execute query with synchronous method, we also assume it takes over 2 seconds for each query
def sfunc(query: Select) -> Sequence[Row[TP]]:
    with Session(engine) as session:
        time.sleep(2)
        return session.execute(query).all()


async def amain():
    return await aiter(afunc)(queries)


def smain():
    return siter(sfunc)(queries)


if __name__ == "__main__":
    format = "%Y-%m-%d %H:%M:%S"

    print(time.strftime(format))

    async_results = asyncio.run(amain())  # it takes ~2 seconds
    print("async users counts:", [len(_) for _ in async_results])

    print(time.strftime(format))

    sync_results = smain()  # it takes ~6 seconds
    print("sync users counts", [len(_) for _ in async_results])

    print(time.strftime(format))
```

Output
```
2024-01-07 22:33:44
async users counts: [3, 3, 3]
2024-01-07 22:33:46
sync users counts [3, 3, 3]
2024-01-07 22:33:52
```
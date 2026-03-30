from functools import singledispatch
from typing import Any


@singledispatch
def handler(item: Any) -> None:
    raise ValueError(f"Unhandled type {type(item)}")


@handler.register
def handle_int(item: int) -> None:
    print(f"Got int - {item}")


@handler.register
def handle_float(item: float) -> None:
    print(f"Got float - {item}")


handler(1)
handler(1.1)
# handler("unknown")

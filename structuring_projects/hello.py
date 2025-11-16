# hello.py
def hello(name: str) -> None:
    print(globals())
    print(locals())
    print(f"Hello, {name}!")


if __name__ == "__main__":
    hello(name="Sebastian")


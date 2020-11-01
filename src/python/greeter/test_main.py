from . import main


def test_greeter_arg() -> None:
    assert main.greet("Tory") == "Hello, Tory"


def test_greeter_kwarg() -> None:
    assert main.greet(name="Tory") == "Hello, Tory"


def test_greeter_default() -> None:
    assert main.greet() == "Hello, Steve"

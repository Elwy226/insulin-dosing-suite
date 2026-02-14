from pathlib import Path
from tests.util import import_module

root_path = Path(__file__).parent.parent
module_path = Path(root_path / "v1.0_complexinsulincalc/complexinsulincalc.py")

complexinsulincalc = import_module(module_path)

def test_get_float(monkeypatch):
    # Prepare the sequence of answers
    inputs = iter([' 42.7    '])

    # Monkeypatch input() so each call gives the next item
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    number = complexinsulincalc.get_float("Enter a number: ")
    assert isinstance(number, float)
    assert number == 42.7
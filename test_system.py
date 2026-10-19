
from unittest.mock import patch
from main import run

def test_system_borrow_book(capsys):
    inputs = ["1", "ISBN001", "U001", "0"]

    with patch("builtins.input", side_effect=inputs):
        run()

    output = capsys.readouterr().out

    assert "Book successfully borrowed" in output


def test_system_return_book(capsys):
    inputs = ["2", "ISBN001", "U001", "0"]

    with patch("builtins.input", side_effect=inputs):
        run()

    output = capsys.readouterr().out

    assert "Book successfully returned" in output

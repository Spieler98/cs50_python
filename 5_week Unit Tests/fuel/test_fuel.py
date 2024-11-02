from fuel import gauge, convert
import pytest

def test_convert():
    assert convert(1, 2) == 50
    assert convert(1, 1) == 100
    assert convert(1, 4) == 25
    assert convert(1, 5) == 20
    assert convert(1, 20) == 5
    assert convert(1, 128) == 0.78125
    with pytest.raises(ZeroDivisionError):
        assert convert(1, 0)


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(5) == "5"
    assert gauge(25) == "25"
    assert gauge(50) == "50"
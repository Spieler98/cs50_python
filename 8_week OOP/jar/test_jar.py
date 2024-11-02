from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    for value in [13, 11, 0]:
        with pytest.raises(ValueError):
            jar.capacity = value

    for value in [13, -1]:
        with pytest.raises(ValueError):
            jar.size = value
            
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 1
    assert jar.deposit(4) == 5
    assert jar.deposit(7) == 12
    with pytest.raises(ValueError):
        assert jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.withdraw(0) == 12
    assert jar.withdraw(3) == 9
    assert jar.withdraw(1) == 8
    assert jar.withdraw(8) == 0
    with pytest.raises(ValueError):
        assert jar.withdraw(1)
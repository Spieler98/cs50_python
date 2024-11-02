from bank import value

def test_value():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("HELLO") == 0
    assert value("H") == 20
    assert value("Hello world!") == 0
    assert value("Goodbye world") == 100
    assert value("why is that") == 100
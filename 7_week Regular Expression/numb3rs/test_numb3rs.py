from numb3rs import validate
import random

def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.0.0.255") == True

    assert validate("256.2.2.2") == False
    assert validate("0.0.0.-1") == False
    assert validate("0.0.0.0.0") == False
    assert validate("0.0.0") == False
    assert validate("0.0.0.0a") == False
    assert validate("a0.0.0.0") == False

def test_gen_validate():
    for _ in range(100000):
        assert validate(gen_ipv4()) == True
        

def gen_ipv4():
    ipv = ""
    counter = 0
    for _ in range(4):
        counter += 1
        rando = random.choice(range(256))
        ipv += "".join(str(rando))
        if counter < 4:
            ipv += "."
    return ipv

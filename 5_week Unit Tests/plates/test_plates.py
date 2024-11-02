from plates import is_valid

def test_is_valid():
    assert is_valid("CS050") == False
    assert is_valid("CS$50") == False
    assert is_valid("CS12345") == False
    
    assert is_valid("CS1234") == True
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS50") == True

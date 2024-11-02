from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("9 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "9:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "9:00 to 17:00"

    assert convert("9:00 PM to 5:00 AM") == "21:00 to 5:00"
    assert convert("0 AM to 12 PM") == "0:00 to 24:00"
    assert convert("12:00 AM to 12 PM") == "0:00 to 24:00"
    assert convert("3 AM to 1:00 PM") == "3:00 to 13:00"
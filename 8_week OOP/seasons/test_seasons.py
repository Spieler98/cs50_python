from seasons import date_delta_minute, date_word
import datetime

today = datetime.date(2024, 12, 30)

def test_delta_minute():
    assert date_delta_minute(datetime.date(2024, 12, 30), today) == 0
    assert date_delta_minute(datetime.date(2024, 11, 30), today) == 43200
    assert date_delta_minute(datetime.date(2020, 12, 30), today) == 2103840
    assert date_delta_minute(datetime.date(2021, 12, 30), today) == 1578240
    assert date_delta_minute(datetime.date(1999, 12, 30), today) == 13150080

def test_date_world():
    assert date_word(2) == "two minutes"
    assert date_word(100) == "one hundred minutes"
    assert date_word(2000) == "two thousand minutes"
    assert date_word(9999) == "nine thousand, nine hundred and ninety-nine minutes"
    assert date_word(-1) == "minus one minutes"

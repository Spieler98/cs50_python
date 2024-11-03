import datetime
import sys
import inflect

def main():
    print(date_word(date_delta_minute(get_date_user(), get_date_today())))

def get_date_user():
    try:
        date_user = input("Date (YYYY-MM-DD): ")
        year,month,day = [int(x) for x in date_user.split("-")]
        return datetime.date(year,month,day)
    except (KeyboardInterrupt, EOFError):
        print("Terminated by user")
        sys.exit()
    except ValueError:
        sys.exit()

def get_date_today():
    return datetime.date.today()

def date_delta_minute(date_user, date_today):
    date_delta_days = abs(date_user - date_today)
    return (date_delta_days.days * 24) * 60

def date_word(minute):
    p = inflect.engine()
    return f"{p.number_to_words(minute)} minutes"

if __name__ == "__main__":
    main()
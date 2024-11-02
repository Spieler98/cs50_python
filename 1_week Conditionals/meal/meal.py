import sys


def main():
    time = input("What time is it? ").strip().lower()

    if time.endswith("a.m."):
        time_converted = convert(time.split(":"), time_format="am")
    elif time.endswith("p.m."):
        time_converted = convert(time.split(":"), time_format="pm")
    else:
        time_converted = convert(time.split(":"))


    if time_converted >= 7.0 and time_converted <= 8.0:
        print("breakfast time")
    elif time_converted >= 12.0 and time_converted <= 13.0:
        print("lunch time")
    elif time_converted >= 18.0 and time_converted <= 19.0:
        print("dinner time")


def convert(time, time_format="default"):
    try:
        if time_format == "default":
            hour, minute = time
            return round((int(hour) + (int(minute)/60)), 2)
        
        elif time_format == "pm":
            time[1] = time[1].replace(" p.m.", "")
            hour = int(time[0])
            minute = int(time[1])
            if hour in range(12):
                hour += 12
            return round((int(hour) + (int(minute)/60)), 2)
        
        elif time_format == "am":
            time[1] = time[1].replace(" a.m.", "")
            hour = int(time[0])
            minute = int(time[1])
            if hour == 12:
                hour = 00
            return round((int(hour) + (int(minute)/60)), 2)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
    main()
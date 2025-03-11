from datetime import datetime, timedelta

bin_day = 2 # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday

def get_next_date(date:datetime, weekday:int):
    days_ahead = (weekday - date.weekday()) % 7
    return (date + timedelta(days=days_ahead)).date()


def main():
    date = datetime.today()
    next_date = get_next_date(date, bin_day)
    print(f"Next bin day is {next_date}")

if __name__ == "__main__":
    main()
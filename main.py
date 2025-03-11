from datetime import datetime, timedelta
from bins import Bins

# Define the colours for each bin type that will show on the Sense HAT
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (148, 0, 211)

# Define the bin day and schedule
bin_day = 2 # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
bin_schedule = {
    "Organics": { "start": datetime(2024,9,4), "frequency": 2, "colour": green },
    "Recycling": { "start": datetime(2024,9,11), "frequency": 2, "colour": yellow },
    "Glass": { "start": datetime(2024,10,16), "frequency": 4, "colour": purple }
}

def main():
    # Obtain the current date to assess the next bin day
    date = datetime.today()

    # Define new bin object
    bin = Bins(bin_day, bin_schedule)

    # Get the next bin details
    next_bin_date = bin.next_bin_date(date)
    bin_type = bin.next_bin_type(next_bin_date)
    print(f"Next {bin_type} bin pickup is on {next_bin_date.strftime("%Y-%m-%d")}")

if __name__ == "__main__":
    main()
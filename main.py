#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from bins import Bins
from sense_hat import SenseHat

# Define the colours for each bin type that will show on the Sense HAT
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (148, 0, 211)
black = (0, 0, 0)

# Define the bin day and schedule
bin_day = 2 # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
bin_schedule = {
    "Organics": { "start": datetime(2024,9,4), "frequency": 2, "colour": green },
    "Recycling": { "start": datetime(2024,9,11), "frequency": 2, "colour": yellow },
    "Glass": { "start": datetime(2024,10,16), "frequency": 4, "colour": purple }
}

def main():
    s = SenseHat()
    s.low_light = True

    # Obtain the current date to assess the next bin day
    date = datetime.today()

    # Define new bin object
    bin = Bins(bin_day, bin_schedule)

    # Get the next bin details
    next_bin_date = bin.next_bin_date(date)
    bin_type = bin.next_bin_type(next_bin_date)
    print(f"Next {bin_type} bin pickup is on {next_bin_date:%Y-%m-%d}")

    # Display the bin type on the Sense HAT
    if bin_type == "Recycling":
        led = bin.sense_hat_pattern(yellow)
    elif bin_type == "Organics":
        led = bin.sense_hat_pattern(green)
    elif bin_type == "Glass":
        led = bin.sense_hat_pattern(purple)
    elif bin_type == "Glass and Organics":
        led = bin.sense_hat_pattern(green, purple)
    else:
        led = bin.sense_hat_pattern(black)

    s.set_pixels(led)

if __name__ == "__main__":
    main()

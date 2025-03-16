#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Program that displays the next bin collection day and type on the Sense HAT.
The program uses the Bins class to determine the next bin collection day and type.
"""

from datetime import datetime
from sense_hat import SenseHat
from bins import Bins

# Define the colours for each bin type that will show on the Sense HAT
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (148, 0, 211)
black = (0, 0, 0)

# Define the bin day and schedule
bin_day = 2  # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
bin_schedule = {
    "Organics": {"start": datetime(2024, 9, 4), "frequency": 2, "colour": green},
    "Recycling": {"start": datetime(2024, 9, 11), "frequency": 2, "colour": yellow},
    "Glass": {"start": datetime(2024, 10, 16), "frequency": 4, "colour": purple}
}


def main():
    # Initialise the Sense HAT object
    s = SenseHat()
    s.low_light = True  # Set the brightness of the LEDs to a lower level
    s.rotation = 180  # Rotate the display 180 degrees

    # Obtain the current date to assess the next bin day
    date = datetime.today()

    # Define new bin object
    bins = Bins(bin_day, bin_schedule)

    # Get the next bin details
    next_bin_date = bins.next_bin_date(date)
    bin_type = bins.next_bin_type(next_bin_date)
    print(f"Next {bin_type} bin pickup is on {next_bin_date:%Y-%m-%d}")

    # Obtain the LED pattern for the bin type
    if bin_type == "Recycling":
        led = bins.sense_hat_pattern(yellow)
    elif bin_type == "Organics":
        led = bins.sense_hat_pattern(green)
    elif bin_type == "Glass":
        led = bins.sense_hat_pattern(purple)
    elif bin_type == "Glass and Organics":
        led = bins.sense_hat_pattern(green, purple)
    else:
        led = bins.sense_hat_pattern(black)

    # Display the bin pattern on the Sense HAT
    s.set_pixels(led)


if __name__ == "__main__":
    main()

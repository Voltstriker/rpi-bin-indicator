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

    # Print the next bin collection day and type
    # If no bin is scheduled, print an error message and display a black LED pattern
    if "No bin" in bin_type:
        print("Error: No bin collection scheduled")
        led = bins.sense_hat_pattern(black)
        return

    # If two bins are scheduled, print both bin types
    if len(bin_type) == 2:
        print(f"Next bin pickup is on {next_bin_date:%Y-%m-%d} for {bin_type[0]} and {bin_type[1]}")
    else:
        print(f"Next bin pickup is on {next_bin_date:%Y-%m-%d} for {bin_type[0]}")

    # Obtain the LED pattern for the bin type
    colour_primary = bin_schedule[bin_type[0]]["colour"]
    colour_secondary = bin_schedule[bin_type[1]]["colour"] if len(bin_type) == 2 else bin_schedule[bin_type[0]]["colour"]

    led = bins.sense_hat_pattern(colour_primary, colour_secondary)

    # Display the bin pattern on the Sense HAT
    s.set_pixels(led)


if __name__ == "__main__":
    main()

"""
A class to represent the bin collection schedule.
"""

from datetime import datetime, timedelta
from typing import List

class Bins:
    """
    A class to represent the bin collection schedule.
    """
    def __init__(self, bin_day:int, bin_schedule:dict) -> None:
        self.bin_day = bin_day # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
        self.bin_schedule = bin_schedule

    def next_bin_date(self, date:datetime) -> datetime:
        """Return the next bin date after the given date.

        :param date: The reference date to start from.
        :type date: datetime
        :return: The next bin date
        :rtype: int
        """
        # Calculate the number of days ahead to the next bin day
        days_ahead = (self.bin_day - date.weekday()) % 7

        # If the bin day is today, check if the bins have already been collected (assume 9am collection time)
        if days_ahead == 0:
            if date.hour >= 9:
                days_ahead = 7
        next_date = date + timedelta(days=days_ahead)

        # Return the date the bin is due to be collected
        return next_date


    def next_bin_type(self, date:datetime) -> List[str]:
        """Return the bin type(s) due for collection on the given date.

        :param date: The date to check for the next bin type.
        :type date: datetime
        :return: The bin type(s) due for collection.
        :rtype: List[str]
        """
        bins_out = []
        # Loop through the bin schedule to determine the bin type(s) due for collection
        for bin_type, schedule in self.bin_schedule.items():
            start_date = schedule["start"]
            frequency = schedule["frequency"]

            # Calculate the number of weeks since the start date
            delta_weeks = (date - start_date).days // 7
            if delta_weeks % frequency == 0:
                bins_out.append(bin_type)

        # If no bins are due, return a message
        if len(bins_out) == 0:
            return ["No bin"]

        return bins_out

    def sense_hat_pattern(self, colour_1: tuple, colour_2: tuple = ()) -> List[tuple]:
        """Return the LED pattern for the Sense HAT based on the bin colours.

        :param colour_1: The primary bin colour.
        :type colour_1: tuple
        :param colour_2: The optional secondary bin colour, defaults to ()
        :type colour_2: tuple, optional
        :return: The LED pattern for the Sense HAT.
        :rtype: List[tuple]
        """
        if colour_2 == (): # If only one bin is due
            colour_2 = colour_1

        # Define the RGB colours for the bin logo
        # pylint: disable=invalid-name
        O = (0, 0, 0) # Black
        P = colour_1 # Primary bin colour
        S = colour_2 # Optional secondary bin colour if two bins are due
        # pylint: enable=invalid-name

        # Create a bin logo pattern for the Sense HAT
        logo = [
            O, O, P, P, P, P, O, O,
            P, P, P, P, P, P, P, P,
            O, P, P, P, P, P, P, O,
            O, P, S, P, P, S, P, O,
            O, P, P, S, S, P, P, O,
            O, P, P, S, S, P, P, O,
            O, P, S, P, P, S, P, O,
            O, P, P, P, P, P, P, O,
        ]

        return logo






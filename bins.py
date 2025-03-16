from datetime import datetime, timedelta

class Bins:
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


    def next_bin_type(self, date:datetime) -> str:
        bins_out = []
        for bin_type, schedule in self.bin_schedule.items():
            start_date = schedule["start"]
            frequency = schedule["frequency"]
            delta_weeks = (date - start_date).days // 7
            if delta_weeks % frequency == 0:
                bins_out.append(bin_type)

        if len(bins_out) == 0:
            return ["No bin"]

        return bins_out

    def sense_hat_pattern(self, colour_1: tuple, colour_2: tuple = ()) -> list:
        if colour_2 == (): # If only one bin is due
            colour_2 = colour_1

        O = (0, 0, 0) # Black
        P = colour_1 # Primary bin colour
        S = colour_2 # Optional secondary bin colour if two bins are due

        # Create a bin logo pattern for the Sense HAT
        logo = [
            O, O, O, O, O, O, O, O,
            O, O, P, P, P, P, O, O,
            P, P, P, P, P, P, P, P,
            O, P, S, P, P, S, P, O,
            O, P, P, S, S, P, P, O,
            O, P, P, S, S, P, P, O,
            O, P, S, P, P, S, P, O,
            O, P, P, P, P, P, P, O,
        ]

        return logo






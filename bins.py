from datetime import datetime, timedelta

class Bins:
    def __init__(self, bin_day:int, bin_schedule:dict) -> None:
        self.bin_day = bin_day # 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
        self.bin_schedule = bin_schedule

    def next_bin_date(self, date:datetime):
        """Return the next bin date after the given date.

        :param date: The reference date to start from.
        :type date: datetime
        :return: The next bin date
        :rtype: int
        """
        # Calculate the number of days ahead to the next bin day
        days_ahead = (self.bin_day - date.weekday()) % 7

        # Return the date the bin is due to be collected
        return (date + timedelta(days=days_ahead))


    def next_bin_type(self, date:datetime):
        bins_out = []
        for bin_type, schedule in self.bin_schedule.items():
            start_date = schedule["start"]
            frequency = schedule["frequency"]
            delta_weeks = (date - start_date).days // 7
            if delta_weeks % frequency == 0:
                bins_out.append(bin_type)

        if "Glass" in bins_out and "Organics" in bins_out:
            return "Glass and Organics"
        elif "Glass" in bins_out:
            return "Glass"
        elif "Organics" in bins_out:
            return "Organics"
        elif "Recycling" in bins_out:
            return "Recycling"
        else:
            return "No bin"




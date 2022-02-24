"""
Entry class

"""
from datetime import date


class Entry:
    """

    """
    def __init__(self,
                 title: str,
                 duration: int,
                 difficulty: int,
                 cur_date: date = date.today()):

        # Header info
        self.title = title         # must have a title
        self.date = cur_date       # Default set to current date.

        # Distance and time data
        self.mileage = None        # Mileage
        self.duration = duration           # Raw time value of exercise

        # Calories burned
        self.calories = None       # Calories burned

        # Difficulty measurements
        self.diff_scale = [0.990, 0.995, 1.00, 1.005, 1.0099]  # Scale factor
        self.difficulty = 0

        # Bounds checking on init
        if difficulty not in [1, 2, 3, 4, 5] and difficulty < 1:
            self.difficulty = 0
        else:  # otherwise, difficulty > 5
            self.difficulty = 5

    def __repr__(self):
        return f"{self.title.upper()}: {self.date}"

    def __eq__(self, other):
        if isinstance(other, Entry):
            return self.title == other.title and \
                   self.date == other.date and \
                   self.mileage == other.mileage and \
                   self.time == other.time and \
                   self.diff_rating == other.diff_rating

    def avg_speed(self) -> float:
        """
        Returns avg speed of the ride.
        :return:
            Returns a float of avg. speed on the ride.
        """
        # s = d / t
        return self.mileage / self.duration

    def get_calories(self, weight: int,
                     lbs_mode: bool = False,) -> int:  # assumes kg
        """
        Returns and sets calories burned for the entry. Assumes entry init

        :param weight:
        :param lbs_mode:
        :return:
        """
        MET = 8     # For cycling application
        if lbs_mode:
            # Conversion: 1 kg = 2.20462262185 lb
            weight = weight * 2.20462262185

            # Calculation
            calories = self.duration * MET * 3.5 * weight / (200 * 60)
            calories = calories * self.diff_scale[self.difficulty - 1]
            self.calories = int(calories)
            return int(calories)

        else:  # kg mode
            # Calculation
            calories = self.duration * MET * 3.5 * weight / (200 * 60)
            calories = calories * self.diff_scale[self.difficulty - 1]
            self.calories = int(calories)
            return int(calories)

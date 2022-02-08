"""
Entry class

"""
from datetime import date


class Entry:

    def __init__(self, name: str, cur_date: date = date.today()):
        self.name = name
        self.date = cur_date

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Entry):
            return self.name == other.name



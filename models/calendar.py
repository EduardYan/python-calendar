"""
This module have the class Calendar
for create a calendar object.
"""

import sys
sys.path.append('.')

from data.days import DAYS, DAYS_LIST


class Calendar:
    """
    Create a Calendar object
    with a days list and a days, like properties.
    """

    def __init__(self, day:str, month:str, year:str):
        # initials values
        self.day = day
        self.year = year
        self.month = month


    def validate_month(self):
        """
        Return list of days for show
        segun the month.

        """

        if self.month == 'Juanary':
            return DAYS[0]
        if self.month == 'February':
            return DAYS[1]
        if self.month == 'March':
            return DAYS[2]
        if self.month == 'April':
            return DAYS[3]
        if self.month == 'May':
            return DAYS[4]
        if self.month == 'June':
            return DAYS[5]
        if self.month == 'July':
            return DAYS[6]
        if self.month == 'August':
            return DAYS[7]
        if self.month == 'September':
            return DAYS[8]
        if self.month == 'October':
            return DAYS[9]
        if self.month == 'November':
            return DAYS[10]
        if self.month == 'December':
            return DAYS[11]


    def show_calendar(self):
        """
        Show the current calendar.
        """

        # calendar for show
        self.calendar = f"""
        |        Calendar         |
        |==========================
        | Year => {self.year}
        | Month => {self.month}
        | Day => {self.day}
        |
        |==========================

        """

        # showing the calendar and the day current
        print(self.calendar)

        # getting the days and show it with tabs
        self.days = self.validate_month()
        # for number_day in self.days:
            # if int(number_day) == self.day:
                # print( '\t\t' + f'{number_day} <== Current Day' )

            # else:
                # print( '\t\t' + number_day, end = '' )
                # print( '\t\t' + '-----' )

        for idx, number_day in enumerate(self.days):
            if int(number_day) == self.day:
                try:
                    print( '\t\t' + DAYS_LIST[idx] + f'{number_day} <== Current Day' )
                except IndexError:
                    print( '\t\t' + DAYS_LIST[idx - int(number_day)] + f'{number_day} <== Current Day' )
                    print( '\t\t' + '-----' )

            else:
                try:
                    print( '\t\t' + DAYS_LIST[idx] + number_day, end = '' )
                    print( '\t\t' + '-----' )

                except IndexError:
                    print( '\t\t' + DAYS_LIST[idx - int(number_day) - 1] + number_day, end = '' )
                    print( '\t\t' + '-----' )

    def __str__(self):
        return self.calendar

"""
This module have the class Calendar
for create a calendar object.
"""

from data.days import DAYS


class Calendar:
    """
    Create a Calendar object
    with a days list and a days, like properties.
    """

    def __init__(self, day:str, month:str, year:str):
        # initials values
        self.number_day = day
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

    def validate_day(self):
        """
        Return the day of the week
        for show it.
        """

        # date_output = check_output('date')
        # search(r'', date_output)
        pass

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
        | Day => {self.number_day}
        |
        |==========================

        """

        # showing the calendar and the day current
        print(self.calendar)

        # getting the days and show it with tabs in the console
        self.number_days_list = self.validate_month()
        for number_day in self.number_days_list:
            if int(number_day) == self.number_day:
                print( '\t\t' + f'{number_day} <== Current Day' )

            else:
                print( '\t\t' + number_day, end = '' )
                print( '\t\t' + '-----' )

    def __str__(self):
        return self.calendar

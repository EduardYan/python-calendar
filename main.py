"""
This is the principal for execute the calendar
program in the terminal with python3.
"""

from models.calendar import Calendar
from datetime import datetime


def validate_month(month:str):
    """
    Validate the moth passed for parameter
    and return the month in string.
    """
    # validating for return the month
    if month == 1:
        return 'January'

    if month == 2:
        return 'February'

    if month == 3:
        return 'March'

    if month == 4:
        return 'April'

    if month == 5:
        return 'May'

    if month == 6:
        return 'June'

    if month == 7:
        return 'July'

    if month == 8:
        return 'August'

    if month == 9:
        return 'September'

    if month == 10:
        return 'October'

    if month == 11:
        return 'November'

    if month == 12:
        return 'December'


def create_calendar():
    """
    Create a calendar object for show in the terminal.
    """

    # getting the date current of the system
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    month = validate_month(month)

    # creating the calendar and show it
    calendar = Calendar(day, month,  year)
    calendar.show_calendar()


if __name__ == '__main__':
    create_calendar()

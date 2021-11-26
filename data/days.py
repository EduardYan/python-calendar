"""
This module have the days of the month
for show it.
"""

# days for use
JANUARY_DAYS = [str(d) for d in range(1, 32)]
FEBRUARY_DAYS = [str(d) for d in range(1, 30)]
MARCH_DAYS = [str(d) for d in range(1, 32)]
APRIL_DAYS = [str(d) for d in range(1, 31)]
MAY_DAYS = [str(d) for d in range(1, 32)]
JUNE_DAYS = [str(d) for d in range(1, 31)]
JULY_DAYS = [str(d) for d in range(1, 32)]
AUGUST_DAYS = [str(d) for d in range(1, 32)]
SEPTEMBER_DAYS = [str(d) for d in range(1, 31)]
OCTOBER_DAYS = [str(d) for d in range(1, 32)]
NOVEMBER_DAYS = [str(d) for d in range(1, 31)]
DECEMBER_DAYS = [str(d) for d in range(1, 32)]

DAYS = (
    JANUARY_DAYS,
    FEBRUARY_DAYS,
    MARCH_DAYS,
    APRIL_DAYS,
    MAY_DAYS,
    JUNE_DAYS,
    JULY_DAYS,
    AUGUST_DAYS,
    SEPTEMBER_DAYS,
    OCTOBER_DAYS,
    NOVEMBER_DAYS,
    DECEMBER_DAYS
)

DAYS_LIST = (
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
)

if __name__ == '__main__':
    print('Testing the days.')

    for days in DAYS:
        print(days)
        print('======================')

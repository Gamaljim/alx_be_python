import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date


def calculate_future_date():
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    current_date = display_current_datetime()
    future_date = current_date.date() + datetime.timedelta(days=number_of_days)

    return future_date



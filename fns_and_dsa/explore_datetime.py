from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date2 = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date2}")
display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    future_date2 = future_date.strftime("%y-%m-%d")
    print(f"Future date: {future_date2}")
calculate_future_date()
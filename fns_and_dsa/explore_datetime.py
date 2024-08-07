from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time!"""

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now()+ timedelta(future_date)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()
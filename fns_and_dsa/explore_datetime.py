from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    try:
        num_days = int(input("Enter number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=num_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {num_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

def main():
    print("Welcome to Date and Time Explorer\n")
    
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()


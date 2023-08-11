import os
from datetime import datetime, timedelta

def create_folders(start_date):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.today()

    folder_name = f"{start_date.strftime(date_format)} - {end_date.strftime(date_format)}"
    os.makedirs(folder_name, exist_ok=True)

if __name__ == "__main__":
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    create_folders(start_date)

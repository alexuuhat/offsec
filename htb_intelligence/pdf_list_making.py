import datetime

# Define the start and end dates
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)

# Open the file in write mode
with open("pdf_dates_list.txt", "w") as file:
    # Iterate over each day in 2020
    current_date = start_date
    while current_date <= end_date:
        # Format the date as YYYY-MM-DD-upload.pdf
        formatted_date = current_date.strftime("%Y-%m-%d") + "-upload.pdf"
        
        # Write the formatted date to the file
        file.write(formatted_date + "\n")
        
        # Move to the next day
        current_date += datetime.timedelta(days=1)

print("Output has been saved to pdf_dates_list.txt")

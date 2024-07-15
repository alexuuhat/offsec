import datetime
import requests
import subprocess

# Function to download file using subprocess
def download_file(url, filename):
    result = subprocess.run(["curl", "-o", filename, url], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading {filename}: {result.stderr}")

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
        
        # Check if the file exists and download it if status code is 200
        url = f"http://intelligence.htb/documents/{formatted_date}" 
        try:
            response = requests.head(url)
            if response.status_code == 200:
                download_file(url, formatted_date)
                print(f"File {formatted_date} downloaded successfully")
        except requests.RequestException as e:
            print(f"Error checking URL {url}: {e}")
        
        # Move to the next day
        current_date += datetime.timedelta(days=1)

print("Output has been saved to pdf_dates_list.txt")

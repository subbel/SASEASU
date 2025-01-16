# import urllib.request
# page = urllib.request.urlopen("http://127.0.0.1:8000/secret/ahdnsdkbakjbkhsdhjsdbkasd928647299")
# f = open("testhtml.html", "w")
# f.write(page.read().decode("utf-8"))
import urllib.request
import csv
import time
from bs4 import BeautifulSoup

def scrape_table(url):
    try:
        # Send a GET request to the URL
        with urllib.request.urlopen(url) as response:
            html_content = response.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table element
        table = soup.find('table')
        if not table:
            print("No table found on the webpage.")
            return []

        # Extract table rows
        rows = table.find_all('tr')
        if not rows:
            print("No rows found in the table.")
            return []

        # Prepare data for comparison
        table_data = []
        for row in rows:
            columns = row.find_all(['th', 'td'])
            row_data = [col.get_text(strip=True) for col in columns]
            table_data.append(row_data)

        return table_data

    except urllib.error.URLError as e:
        print(f"An error occurred while fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def read_existing_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def append_new_data_to_csv(file_path, new_data):
    try:
        existing_data = read_existing_csv(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in new_data:
                if row not in existing_data:
                    writer.writerow(row)
    except Exception as e:
        print(f"An error occurred while updating the CSV file: {e}")

def main(url, output_file):
    while True:
        print("Fetching and comparing data...")
        new_data = scrape_table(url)
        if new_data:
            append_new_data_to_csv(output_file, new_data)
        print("Waiting for 2 minutes before the next fetch...")
        time.sleep(120)

# URL and output file
url = "http://127.0.0.1:8000/secret/ahdnsdkbakjbkhsdhjsdbkasd928647299"
output_file = "table_data.csv"

# Start the loop
main(url, output_file)

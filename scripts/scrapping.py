import requests
from bs4 import BeautifulSoup
import csv
import os

# Ensure the data directory exists
os.makedirs("../data", exist_ok=True)

# File paths for saving data
CSV_FILE = "../data/infopark_jobs.csv"
FILTERED_CSV_FILE = "../data/infopark_python_php_jobs.csv"

def scrape_jobs():
    url = "http://infopark.in/companies/job-search"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data from the website")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="row company-list joblist")

    if not jobs:
        print("No job listings found. The page structure might have changed.")
        return

    all_jobs = []
    filtered_jobs = []

    for job in jobs:
        # Extract job title and link
        title_elem = job.find("a")
        title = title_elem.text.strip() if title_elem else "N/A"
        link = title_elem["href"].strip() if title_elem else "#"

        # Extract company name
        company_elem = job.find("h4")
        company = company_elem.text.strip() if company_elem else "N/A"

        # Extract posted date
        date_elem = job.find("span", class_="job-date")
        posted_date = date_elem.text.strip() if date_elem else "N/A"

        # Default location
        location = "Kochi, India"

        # Store the job data
        job_data = [title, company, location, posted_date, f"http://infopark.in{link}"]
        all_jobs.append(job_data)

        # Filter for Python and PHP jobs
        if "python" in title.lower() or "php" in title.lower():
            filtered_jobs.append(job_data)

    # Save all jobs to a CSV file
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Posted Date", "Application Link"])
        writer.writerows(all_jobs)

    print(f"All job data saved to {CSV_FILE}")

    # Save filtered jobs to a separate CSV file
    with open(FILTERED_CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Posted Date", "Application Link"])
        writer.writerows(filtered_jobs)

    print(f"Filtered Python and PHP jobs saved to {FILTERED_CSV_FILE}")

if __name__ == "__main__":
    scrape_jobs()

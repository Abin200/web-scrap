import csv

def save_to_csv(job_listings, output_file="infopark_jobs.csv"):
    """
    Save job data to a CSV file.

    Parameters:
        job_listings (list): A list of dictionaries containing job details.
        output_file (str): The filename of the CSV file to save the data.
    """
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["Job Title", "Company Name", "Location", "Posted Date", "Description", "Application Link"])
        
        # Write job details
        for job in job_listings:
            writer.writerow([
                job.get("title", "N/A"),
                job.get("company_name", "N/A"),
                job.get("location", "N/A"),
                job.get("posted_date", "N/A"),
                job.get("description", "N/A"),
                job.get("application_link", "N/A")
            ])
    print(f"Data successfully saved to {output_file}")

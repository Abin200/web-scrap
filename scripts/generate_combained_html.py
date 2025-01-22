import os
import csv

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(BASE_DIR, "../templates/index.html")
CSV_FILE = os.path.join(BASE_DIR, "../data/infopark_jobs.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "../output/combined_jobs.html")

# Ensure the output directory exists
os.makedirs(os.path.join(BASE_DIR, "../output"), exist_ok=True)

def generate_html():
    """
    Combines the job data CSV with the HTML template.
    """
    # Read the CSV file
    table_rows = ""
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            table_rows += f"""
            <tr>
                <td>{row['Job Title']}</td>
                <td>{row['Company Name']}</td>
                <td>{row['Location']}</td>
                <td>{row['Posted Date']}</td>
                <td><a href="{row['Application Link']}" target="_blank">Apply Now</a></td>
            </tr>
            """

    # Load the HTML template
    with open(TEMPLATE_FILE, mode="r", encoding="utf-8") as file:
        html_content = file.read()

    # Replace the placeholder with the actual job data
    html_content = html_content.replace("{{JOB_DATA}}", table_rows)

    # Write the final HTML file
    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Generated HTML: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_html()


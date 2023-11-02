import csv
import re

# python3 /Users/alexpieroni/Documents/Proj/RemoveDuplicateEmails/main.py

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)


def remove_duplicates_from_csv(input_filename, output_filename):
    seen_emails = set()
    unique_rows = []

    with open(input_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            email = row[0]
            # check unique and valid form
            if email not in seen_emails and is_valid_email(email):
                seen_emails.add(email)
                unique_rows.append(row)

    # write
    with open(output_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(unique_rows)

input_filename = "input.csv" #modify as needed
output_filename = "output.csv" #modify as needed
remove_duplicates_from_csv(input_filename, output_filename)

import json
import re
import inflect
from .pdf_utils import extract_text_from_pdf, extract_tables_from_pdf

# Initialize inflect engine for handling numbers in words
p = inflect.engine()

def extract_data_from_pdf(file_path, template_path):
    # Load the extraction template from the JSON file
    with open(template_path, 'r') as json_file:
        extraction_template = json.load(json_file)

    # Extract text and tables from the PDF document
    text = extract_text_from_pdf(file_path)
    tables = extract_tables_from_pdf(file_path)

    # Extract data using the extraction template
    extracted_data = {}

    # Extract header data
    for field, rules in extraction_template["Header Extraction"].items():
        for rule in rules["rules"]:
            match = re.search(rule, text)
            if match:
                extracted_data[field] = match.group(1)
                break

    # Extract table data
    line_items = []
    for table in tables:
        for row in table:
            line_item = {}
            # Extract data from the table row and add it to the line_item dictionary
            # The specific code you need to add will depend on the format of the table data
            if len(row) >= 4:
                line_item["Item"] = row[0]
                line_item["Quantity"] = row[1]
                line_item["Price"] = row[2]
                line_item["Total"] = row[3]
                line_items.append(line_item)
            else:
                print(f"Skipping row with insufficient data: {row}")

    # Separate invoice number, customer number, and date from the other data
    invoice_data = line_items.pop(1)
    extracted_data["Invoice Number"] = invoice_data["Item"]
    extracted_data["Customer Number"] = invoice_data["Quantity"]
    extracted_data["Tenure"] = invoice_data["Price"]
    extracted_data["Date"] = invoice_data["Total"]

    extracted_data["Line Items"] = line_items

    return extracted_data

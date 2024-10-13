import json

def create_generalized_template():
    # Generalized template for header extraction
    header_template = {
        "Invoice Number": {"rules": ["Find 'Invoice No', 'Invoice #' or 'Bill No' and extract the value"]},
        "Invoice Date": {"rules": ["Find 'Invoice Date' or 'Date of Issue' and extract the date in multiple formats (DD.MM.YYYY, MM/DD/YYYY)"]},
        "Vendor Name": {"rules": ["Find 'Vendor Name', 'Supplier', or 'Company Name' and extract the text value"]},
        "Total Amount": {"rules": ["Find 'Total Amount', 'Amount Due', or 'Invoice Amount' and extract the numeric value"]}
    }

    # Generalized template for table data extraction (line items)
    table_template = {
        "Line Items": {
            "columns": {
                "Item": {"rules": ["Identify 'Item', 'Description', or 'Product' column and extract the item name"]},
                "Quantity": {"rules": ["Find 'Qty', 'Quantity', or 'Units' and extract the numeric value"]},
                "Price": {"rules": ["Find 'Price', 'Unit Price', or 'Rate' and extract the numeric value"]},
                "Total": {"rules": ["Find 'Total', 'Amount', or 'Line Total' and extract the calculated value"]}
            }
        }
    }

    # Combining both generalized templates into one dictionary
    extraction_template = {
        "Header Extraction": header_template,
        "Table Extraction": table_template
    }

    # Saving the generalized template to a JSON file
    with open('generalized_extraction_template.json', 'w') as json_file:
        json.dump(extraction_template, json_file, indent=4)

    print("Generalized extraction template JSON has been created successfully!")

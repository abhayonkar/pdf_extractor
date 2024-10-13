import json
import regex as re  # Using regex instead of re for better performance
import pdfplumber
import pytesseract
from pdf2image import convert_from_path  # To convert PDF pages to images for OCR
from pytesseract import Output


def extract_data_from_pdf(file_path):
    try:
        invoice_details = {}
        line_items = {}

        with pdfplumber.open(file_path) as pdf_file:
            for page in pdf_file.pages:
                text = page.extract_text()
                tables = page.extract_tables()

                if text:
                    # Extract Invoice Details
                    invoice_date_match = re.search(r'Invoice Date:\s*(\d{2}\.\d{2}\.\d{4})', text)
                    if invoice_date_match:
                        invoice_details["Invoice Date"] = invoice_date_match.group(1)

                    invoice_number_match = re.search(r'Invoice(?: No| #):\s*([\w/]+)', text)
                    if invoice_number_match:
                        invoice_details["Invoice Number"] = invoice_number_match.group(1)

                    vendor_name_match = re.search(r'Vendor Name:\s*(.+)', text)
                    if vendor_name_match:
                        invoice_details["Vendor Name"] = vendor_name_match.group(1)

                    total_amount_match = re.search(r'Total Amount:\s*([\d.,]+)', text)
                    if total_amount_match:
                        invoice_details["Total Amount"] = total_amount_match.group(1)
                    else:
                        print("Warning: Total Amount not found in the text.")

                    # Extract Line Items
                    line_item_matches = re.finditer(r'(Item: [\w/]+)\s*Price:\s*([\d.,]+)', text)
                    for match in line_item_matches:
                        item = match.group(1)
                        price = match.group(2)
                        line_items[item] = line_items.get(item, 0) + float(price.replace(',', ''))

                # If table extraction fails, fall back to OCR
                if not tables:
                    print("Falling back to OCR for table extraction...")
                    tables = extract_table_using_ocr(page)

                # Print extracted tables for debugging
                print("Extracted Tables:")
                print(tables)

        # Return extracted data
        return {"Invoice Details": invoice_details, "Line Items": line_items}

    except Exception as e:
        print(f"An error occurred while processing the PDF file: {e}")


def extract_table_using_ocr(page):
    """ Use OCR to extract table data from a PDF page if direct extraction fails. """
    image = page.to_image().original  # Convert page to image format for OCR
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    # Simple approach to extract lines of text (this can be enhanced further)
    rows = []
    row = []
    for i, word in enumerate(data['text']):
        if word.strip():
            row.append(word)
        if data['block_num'][i] > 1:  # Assuming a new block means a new row in table
            if row:
                rows.append(row)
                row = []

    if row:  # Add the last row if any
        rows.append(row)

    return rows


def main():
    print("\nExtract data from PDF:")
    result = extract_data_from_pdf('data/sample-invoice.pdf')
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()

Here's an example of a `README.md` file that explains the thought process and assumptions made for the program:

# PDF Data Extraction Program

This program is designed to extract data from a PDF document containing invoice information. The program uses a JSON template to define the rules for extracting data from the document, and it outputs the extracted data in JSON format.

## Thought Process

The program was developed with the following thought process:

1. Understand the structure and format of the PDF document containing invoice information.
2. Identify the key data points that need to be extracted from the document, such as invoice number, customer number, date, and line items.
3. Create a JSON template that defines the rules for extracting each data point from the document.
4. Implement a Python program that uses the JSON template to extract the data from the PDF document.
5. Handle any variations in the format of the document, such as missing data or different table structures.

## Assumptions

The following assumptions were made during the development of the program:

1. The PDF document contains a single page with a table containing the line items.
2. The table containing the line items has a consistent structure, with each row representing a line item and containing columns for item, quantity, price, and total.
3. The invoice number, customer number, and date are located in the second row of the table.
4. The vendor name is located in the text of the document and can be extracted using a regular expression.
5. The program is designed to handle variations in the format of the document, such as missing data or different table structures, but it may not be able to handle all possible variations.

## Usage

To use the program, follow these steps:
0. Activate the virtualenv named 'assignment'
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Create a JSON template that defines the rules for extracting data from the PDF document.
3. Run the program using the command `python main.py <input_pdf> <template_json> <output_json>`, where `<input_pdf>` is the path to the input PDF document, `<template_json>` is the path to the JSON template, and `<output_json>` is the path to the output JSON file.

Ex: " python main.py data/sample-invoice.pdf templates/generalized_extraction_template.json output/extracted_data_test.json"

## Limitations

The program has the following limitations:

1. The program is designed to handle a single page with a table containing the line items. It may not be able to handle multi-page documents or documents with a different layout.
2. The program assumes that the table containing the line items has a consistent structure. If the structure of the table varies between documents, the program may not be able to extract the data correctly.
3. The program assumes that the invoice number, customer number, and date are located in the second row of the table. If the location of this data varies between documents, the program may not be able to extract the data correctly.
4. The program assumes that the vendor name is located in the text of the document and can be extracted using a regular expression. If the vendor name is not located in the text of the document or if it is not in a format that can be extracted using a regular expression, the program may not be able to extract the data correctly.

\complete.# pdf_extractor

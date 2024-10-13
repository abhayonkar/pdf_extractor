import os
import json
import argparse
from modules.extraction_logic import extract_data_from_pdf

def main():
    parser = argparse.ArgumentParser(description="Extract data from a PDF document using a JSON template.")
    parser.add_argument("input_pdf", help="Path to the input PDF document")
    parser.add_argument("template_json", help="Path to the JSON template for data extraction")
    parser.add_argument("output_json", help="Path to the output JSON file")
    args = parser.parse_args()

    # Create the output directory if it does not exist
    output_dir = os.path.dirname(args.output_json)
    os.makedirs(output_dir, exist_ok=True)

    extracted_data = extract_data_from_pdf(args.input_pdf, args.template_json)

    with open(args.output_json, 'w') as json_file:
        json.dump(extracted_data, json_file, indent=4)

    print(f"Data extracted successfully and saved to {args.output_json}")

if __name__ == "__main__":
    main()

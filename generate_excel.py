"""
This bit of pythoncode I used it to generate Excel files (.xlxs files) for all the jsonl files in the massive data set
"""
import os
import pandas as pd
import json

jsonl_files_dir = "D:/CodingProjects/PythonProjects/1.1/data"

output_folder = "D:/CodingProjects/PythonProjects/languages_output"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all JSON Lines files in the directory
jsonl_files = [f for f in os.listdir(jsonl_files_dir) if f.endswith(".jsonl")]

# Iterate through each JSON Lines file
for jsonl_file in jsonl_files:
    # Create a full path to the JSON Lines file
    jsonl_file_path = os.path.join(jsonl_files_dir, jsonl_file)

    # Extract language code from file name
    language_code = os.path.splitext(jsonl_file)[0]

    # Load the JSON Lines data into a DataFrame
    data = []
    with open(jsonl_file_path, "r", encoding="utf-8") as jsonl_file:
        for line in jsonl_file:
            data.append(json.loads(line))

    # Create a DataFrame from the loaded data
    df = pd.DataFrame(data)

    # Specify the path to save the Excel file for the language in the output folder
    xlsx_file_path = os.path.join(output_folder, f"{language_code}.xlsx")

    # Save the DataFrame as an Excel file in the output folder
    df.to_excel(xlsx_file_path, index=False)

    print(f"Excel file for {language_code} has been generated and saved to {xlsx_file_path}.")

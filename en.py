"""
This code I used it on trial to generate an xlxs file for en-US.jsonl file.
"""

import os
import pandas as pd
import json

# Path to the extracted JSON Lines file
jsonl_file_path = "D:/CodingProjects/PythonProjects/output_folder/en-US.jsonl/1.1/data/en-US.jsonl"

# Load the JSON Lines data into a DataFrame
data = []
with open(jsonl_file_path, "r", encoding="utf-8") as jsonl_file:
    for line in jsonl_file:
        data.append(json.loads(line))

# Create a DataFrame from the loaded data
df = pd.DataFrame(data)

# Specify the path to save the Excel file
xlsx_file_path = "D:/CodingProjects/PythonProjects/output_folder/en-xx.xlsx"

# Save the DataFrame as an Excel file
df.to_excel(xlsx_file_path, index=False)

print(f"Excel file has been generated and saved to {xlsx_file_path}.")

"""
import zipfile
import os

zip_file_path = "D:/CodingProjects/PythonProjects/amazon-massive-dataset-1.1_CAT1.tar.zip"
output_folder = "D:/CodingProjects/PythonProjects/output_folder"  # Specify the output folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Extract en-US.jsonl from the Zip archive to the output folder
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract("1.1/data/en-US.jsonl", os.path.join(output_folder, "en-US.jsonl"))

print(f"File en-US.jsonl has been extracted to {output_folder}.")
"""
"""
The commented code abpve is code number 2 I tried
"""



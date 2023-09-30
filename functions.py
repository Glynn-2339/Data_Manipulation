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
The above code will extract the en-US.jsonl and place it into the "out_put folder"
"""

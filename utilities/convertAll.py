# pptToPDF
# Created by: Aaron Jones
# Sourced from https://codingshiksha.com/python/python-3-script-to-convert-all-pptx-files-in-directory-to-pdf-documents-in-command-line-full-project-for-beginners/
# Description: The purpose of this script is to create a python script to convert pptx to pdf. 
#              to better convert and implement PowerPoint presentations to PDF's to display them
#              on a website easier.
# Usage: python.exe ConvertAll.py input-folder output-folder
import sys
import os
import comtypes.client

input_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]

input_folder_path = os.path.abspath(input_folder_path)
output_folder_path = os.path.abspath(output_folder_path)

input_file_paths = os.listdir(input_folder_path)

for input_file_name in input_file_paths:
    
    # Skip if file does not contain a power point extension
    if not input_file_name.lower().endswith((".ppt", ".pptx")):
        continue

    # Create input file path
    input_file_path = os.path.join(input_folder_path, input_file_name)

    # Create powerpoint application object
    powerpoint = comtypes.client.CreatObject("Powerpoint.Application")

    # Set visibility to minimize
    powerpoint.Visible = 1

    # Open the powerpoint slides
    slides = powerpoint.Presentations.Open(input_file_path)

    # Get base file name
    file_name = os.path.splitext(input_file_name) #[0]

    # Create output file path
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")

    # Save as PDF (formatType = 32)
    slides.SaveAs(output_file_path, 32)

    # Close the slide deck
    slides.Close()

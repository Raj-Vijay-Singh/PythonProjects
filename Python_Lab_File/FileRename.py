import os
import glob

# Get all files that start with "P" and have a pattern like "P<number>_"
files = glob.glob("P*_*.py")  # Adjust file extension if necessary

# Loop through the files and rename them in correct sequence
for index, old_name in enumerate(files, start=1):
    # Split the old name to get the main part after 'P<number>_'
    base_name = old_name.split('_')[1]

    # Create the new name with correct numbering
    if index < 10:
        new_name = f"P0{index}_{base_name}"
    else:
        new_name = f"P{index}_{base_name}"

    # Rename the file
    os.rename(old_name, new_name)
    print(f"Renamed: {old_name} -> {new_name}")
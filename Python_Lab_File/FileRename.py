import os
import glob

files = glob.glob("P*_*.py")

for index, old_name in enumerate(files, start=1):
    base_name = old_name.split('_')[1]

    if index < 10:
        new_name = f"P0{index}_{base_name}"
    else:
        new_name = f"P{index}_{base_name}"

    os.rename(old_name, new_name)
    print(f"Renamed: {old_name} -> {new_name}")
# Import required modules
import os
import shutil

# -------------------------------
# Step 1: Create and Write File
# -------------------------------

try:
    # Open file in write mode
    file = open("sample.txt", "w")

    # Write content into file
    file.write("Hello, this is a Python File Handling Project.\n")
    file.write("This file is created for internship task.")

    # Close file
    file.close()

    print("File created and data written successfully.")

except Exception as e:
    print("Error while writing file:", e)

# -------------------------------
# Step 2: Read File Content
# -------------------------------

try:
    # Open file in read mode
    file = open("sample.txt", "r")

    # Read content
    content = file.read()

    print("\nFile Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error while reading file:", e)

# -------------------------------
# Step 3: Rename File
# -------------------------------

try:
    # Rename sample.txt to new_sample.txt
    os.rename("sample.txt", "new_sample.txt")

    print("\nFile renamed successfully.")

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error while renaming file:", e)

# -------------------------------
# Step 4: Move File to Folder
# -------------------------------

try:
    # Create folder if not exists
    folder_name = "MovedFiles"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Move file into folder
    shutil.move("new_sample.txt", f"{folder_name}/new_sample.txt")

    print("File moved successfully.")

except Exception as e:
    print("Error while moving file:", e)

# -------------------------------
# Step 5: Delete File
# -------------------------------

try:
    # Delete the moved file
    os.remove(f"{folder_name}/new_sample.txt")

    print("File deleted successfully.")

except FileNotFoundError:
    print("File already deleted.")

except Exception as e:
    print("Error while deleting file:", e)

# -------------------------------
# Project Completed
# -------------------------------

print("\nPython File Handling & Automation Task Completed.")
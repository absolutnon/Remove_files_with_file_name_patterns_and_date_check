from ast import pattern
from importlib.resources import path
import os
from pathlib import Path
import re
import time
import shutil

def main():
    delete_file_count = 0
    #file_path = "D:/Media/"
    file_path = "C:/Users/Pahuton.Sriwichai/OneDrive - GB News/Documents/RemoveMediaFiles/"
    patterns = [r"^([\w]{8})-([\w]{4})-([\w]{4})-([\w]{4})-([\w]{12})\.\w+", r"^storage_manager[\w\.\-]+gz$"]
    days = 0.001
    matched_file = []

    #get current time and convert to seconds
    current_in_seconds = time.time() - (days * 24 * 60 * 60)

    for pattern in patterns:
        delete_file_count = 0
        matched_file = search_file_with_regex(file_path, pattern)
        
        for file in matched_file:
            file_age = get_file_age(file_path, file)
            if current_in_seconds >= file_age:
                remove_file(file_path, file)
                delete_file_count += 1
    
        print("Total files delete: " + str(delete_file_count))

def remove_file(Path, file):
    # removing the file
	if not os.remove(Path + file):
		# success message
		print(f"{Path} {file} is removed successfully")
	else:
		# failure message
		print(f"Unable to delete the {Path} {file}")

def search_file_with_regex(Path, Pattern):
    files = []
    # search through files in directory
    for file in os.listdir(Path):
        
        # Check if file name pattern matched to the regex
        if re.search(Pattern, file):
            files.append(file)        
    
    return files

def get_file_age(file_path, file):
    # getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(file_path + file).st_ctime

	# returning the time
	return ctime

if __name__ == '__main__':
    main()
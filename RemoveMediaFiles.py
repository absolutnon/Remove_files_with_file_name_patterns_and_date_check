import os
import re
import os.path as path
import time
import datetime

file_path = "D:/Media/"
pattern = r"^([\w]{8})-([\w]{4})-([\w]{4})-([\w]{4})-([\w]{12})\.[mp4|MOV|mov|MP4|mxf|MXF]"
day_limit = 14
result = []
removed_files = []

def remove_media(file_pattern, path_to_file):
    counter = 0
    for file in os.listdir(path_to_file):
        if re.search(file_pattern, file):
            result.append(file)                 #just put the matched search to result list
            #call check files older than function to check if file that matched to the pattern are older than the specified amount, if yes, remove them
            if check_date_older_than(file_path + file, day_limit):
                removed_files.append(file)      #Add removed fils to a list
                os.remove(file_path + file)     #remove file that already if it's older than specify date limit
                counter += 1
                log_deleted_files(file)         #recall create deleted log function
                print(file_path + file)
    file_total = "Total file deleted: " + str(counter) + " files"
    log_deleted_files(file_total)

def check_date_older_than(file, days):
    file_time = path.getctime(file)
    # Return true or false if file is older than number of days put in the input
    return ((time.time() - file_time) / 3600 > 24*days)

def log_deleted_files(file_removed):
    #create a text file that displays all the files that deleted
    with open(r'D:/Removed_files_' + datetime.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p") + '.txt', 'a', newline='') as file_rm:
        file_rm.writelines(file_removed + "\n")

#recall function to do the file search, remove and create logs
remove_media(pattern, file_path)



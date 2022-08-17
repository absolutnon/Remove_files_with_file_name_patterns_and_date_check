import os
import re
import os.path as path
import time
import datetime

#file_path = "D:/Media/"
file_path = "C:/Users/Pahuton.Sriwichai/OneDrive - GB News/Documents/RemoveMediaFiles/"
pattern = r"^([\w]{8})-([\w]{4})-([\w]{4})-([\w]{4})-([\w]{12})\.\w+"
pattern_stgmgrlog = r"^storage_manager[\w\.\-]+gz$"
day_limit = 0.001
result = []
removed_files = []

def remove_media(file_pattern, path_to_file, file_prefix):
    counter = 0
    for file in os.listdir(path_to_file):
        if re.search(file_pattern, file):
            #call check files older than function to check if file that matched to the pattern are older than the specified amount, if yes, remove them
            if check_date_older_than(file_path + file, day_limit):
                os.remove(file_path + file)     #remove file that already if it's older than specify date limit
                counter += 1
                log_deleted_files(file, file_prefix)         #recall create deleted log function
                print(file_path + file)
    file_total = "Total files deleted: " + str(counter) + " files"
    print(file_total)
    log_deleted_files(file_total, file_prefix)

def check_date_older_than(file, days):
    #file_time = path.getctime(file)
    today=datetime.datetime.now()# it will get currunt datetime and transfer to variable(today)
    print(str(today))
    file_time=datetime.datetime.fromtimestamp(os.path.getctime(file))# Here, fortimestamp will get the date of file created 
    print(str(file_time))
    dif_days=(today-file_time).days
    print(str(dif_days))
    if dif_days > days:
        return True
    else: 
        return False
    # Return true or false if file is older than number of days put in the input
    #return ((time.time() - file_time) / 3600 > 24*days)

def log_deleted_files(file_removed, filename_prefix):
    #create a text file that displays all the files that deleted
    with open(r"C:/logs/" + filename_prefix + "_files_" + datetime.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p") + '.txt', 'a') as file_rm:
        file_rm.writelines(file_removed + "\n")

#recall function to do the file search, remove and create logs
#remove_media(pattern, file_path, "Remove_media_")
#remove_media(pattern_stgmgrlog, file_path, "Remove_logs_")
check_date_older_than("C:/Users/Pahuton.Sriwichai/OneDrive - GB News/Documents/RemoveMediaFiles/storage_manager-2022-07-06.log.19.gz", 1)



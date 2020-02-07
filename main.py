from datetime import datetime
from constants import *
from actions import sendEmail

error_found = False
#today = datetime.today().strftime(DATE_FORMAT)  # for linux
counter = 0
errors_list = []
is_empty = False
index = False

if ENABLE == True:
    day = datetime.today().strftime(DATE_FORMAT)  # for windows

    filename = ''.join(
        (LOGS_FOLDER_PATH, LOG_FILE_BASE_NAME, day, LOG_FILE_EXTENSION))

    index_filename = ''.join(
        (INDEX_LOG_NAME_PATH, filename, INDEX_LOG_NAME, LOG_FILE_EXTENSION))

    with open(index_filename, "a+") as f:
        f.seek(0)
        first_char = f.read(1)
        if not first_char:
            is_empty = True  # file is empty
        else:
            index = f.readline()

    with open(filename) as file:

        if index != False:
            for i in xrange(6):
                file.next()

        for line in file:
            index = index + 1
            for word in WORD_LIST:
                if word in line:
                    error_found = True
                    counter = counter + 1
                    errors_list.append(line)

    with open(index_filename, "w") as f:
        f.write(counter)

    sendEmail(errors_list)
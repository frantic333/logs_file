#!/bin/python3
# Менеджмент лог файлов
# > python logs.py(название скрипта) mylog.txt(название лог файла) 10(допустимый максимальный размер лог файла) 5(дополнительно создаваемые лог файлы)



import shutil          #For CopyFile
import os              #For GetFileSize and Check If File exists
import sys             #For CLI Arquments

# logs.py mylog.txt 10 5

#Если аргументов в команде меньще 4, то выведется соответствующее сообщение
if(len(sys.argv) < 4):
    print("Missing arguments! Usage is script.py 10 5")
    exit(1)

file_name  = sys.argv[1]
limitsize  = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):             #Check if MAIN logfile exist
    logfile_size = os.stat(file_name).st_size      #Get Filesize in bytes
    logfile_size = logfile_size / 1024             #Convert from bytes to kilobytes

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum - 1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied" + src + "to" + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copied" + file_name + " to " + file_name + "_")
        my_file = open(file_name, 'w')
        my_file.close()
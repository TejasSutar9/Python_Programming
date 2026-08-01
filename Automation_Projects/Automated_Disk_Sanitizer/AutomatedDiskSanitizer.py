###############################################################
#
#   Importing required libraries
#
###############################################################

import sys
import os
import time
import hashlib
import schedule

###############################################################
#
#   Function :          CalculateCheckSum
#   Input :             Name of File
#   Description :       Returns MD5 checksum of a file
#   Date :              26/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

def CalculateCheckSum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

###############################################################
#
#   Function :          FindDuplicate
#   Input :             Name of Directory
#   Description :       Finds duplicate files using checksum
#   Date :              26/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

def FindDuplicate(DirectoryName):

    if(os.path.exists(DirectoryName) == False):
        print("Directory Automation Error : Path is invalid")
        return None

    if(os.path.isdir(DirectoryName) == False):
        print("Directory Automation Error : It is not a directory")
        return None

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

###############################################################
#
#   Function :          DeleteDuplicate
#   Input :             Name of Directory
#   Description :       Deletes duplicate files and creates log
#   Date :              26/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

def DeleteDuplicate(DirectoryName):

    Border = "_" * 50

    timestamp = time.ctime()

    LogFileName = "DuplicateFileLog_%s.log" % (timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    print("Log file created :", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Automated Disk Sanitizer\n")
    fobj.write(Border + "\n\n")

    fobj.write("Scanning Directory : " + DirectoryName + "\n")
    fobj.write("Started At : " + timestamp + "\n\n")

    MyDict = FindDuplicate(DirectoryName)

    if(MyDict == None):
        fobj.close()
        return
    
    # Count files BEFORE deleting duplicates
    
    TotalFiles = 0
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
            TotalFiles = TotalFiles + len(FileName)
            

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    TotalDeleted = 0
    TotalGroups = len(Result)

    fobj.write(Border + "\n")
    fobj.write("Duplicate Files\n")
    fobj.write(Border + "\n\n")

    for value in Result:

        KeepFirst = True

        for subvalue in value:

            if(KeepFirst):
                fobj.write("Original : " + subvalue + "\n")
                KeepFirst = False
            else:
                fobj.write("Deleted  : " + subvalue + "\n")
                os.remove(subvalue)
                TotalDeleted = TotalDeleted + 1

        fobj.write("\n")


    fobj.write(Border + "\n")
    fobj.write(f"Total Files Scanned : {TotalFiles}\n")
    fobj.write(f"Duplicate Groups    : {TotalGroups}\n")
    fobj.write(f"Files Deleted       : {TotalDeleted}\n")
    fobj.write(Border + "\n")

    fobj.write("Completed At : " + time.ctime())
    fobj.write("\n" + Border + "\n")

    fobj.close()

    print("Total deleted files :", TotalDeleted)

###############################################################
#
#   Function name :     main
#   Input :             Command line arguments
#   Description :       It controls the script
#   Date :              26/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

def main():

    Border = "-" * 60

    print(Border)
    print("Automated Disk Sanitizer")
    print(Border)

    # Handle --h and --u when only one argument is passed.
    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script finds and deletes duplicate files.")
            print("It scans the given directory recursively,")
            print("keeps the first copy and deletes duplicate files.")
            print("A log file is generated after every scan.")
            

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage :")
            print("python AutomatedDiskSanitizer.py DirectoryPath TimeInMinutes")
            print()
            print("Example :")
            print('python AutomatedDiskSanitizer.py "D:\\TestFolder" 5')
            
        else:

            print("Missing Time Interval.")
            print("Usage :")
            print("python AutomatedDiskSanitizer.py DirectoryPath TimeInMinutes")
            return
            
    # Normal execution requires exactly 3 arguments.
    elif(len(sys.argv) == 3):

        try:

            TimeInterval = int(sys.argv[2])

            if(TimeInterval <= 0):

                print("Please enter a valid positive time interval.")
                return

        except ValueError:

            print("Time interval should be an integer.")
            return

        print(f"Scanning '{sys.argv[1]}' every {TimeInterval} minute(s)...")
        print("Press Ctrl + C to stop the automation.\n")

        schedule.every(TimeInterval).minutes.do(DeleteDuplicate, sys.argv[1])
        
         # Handle Ctrl + C gracefully
        try:

            while(True):

                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:

            print("\nAutomation stopped by user.")

    # Invalid number of arguments
    else:

        print("Invalid number of arguments")
        print("Use --h or --u for more information")

    print(Border)
    print("Thank you for using Automated Disk Sanitizer")
    print(Border)

###############################################################
#
#   Starter of the automation script
#
###############################################################

if __name__ == "__main__":
    main()
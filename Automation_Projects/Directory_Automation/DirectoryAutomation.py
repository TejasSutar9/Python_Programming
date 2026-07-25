###############################################################
#
#   Importing required libraries
#
###############################################################

import sys             # Used to accept command line arguments
import os              # Used for directory and file operations
import time            # Used to get current date & time
import schedule        # Used to execute the function repeatedly after a fixed interval

###############################################################
#
#   Function name :     DirectoryScanner
#   Input :             Name of Directory
#   Description :       Deletes all empty files periodically
#   Date :              19/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

# Business Logic Function
# Scans the directory, creates a log file, finds empty files and deletes them
def DirectoryScanner(DirectoryPath):

    Border = "_" * 40

    timestamp = time.ctime()

    LogFileName = "DirectoryAutomationLog_%s.log" % (timestamp)

    LogFileName = LogFileName.replace(" ", "_")

    LogFileName = LogFileName.replace(":", "_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Directory Automation Error : There is no such directory with name", DirectoryPath)
        return        

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Directory Automation Error : It is not a directory with name", DirectoryPath)
        return        
    
    
    print("Log file gets created with name :", LogFileName)


    fobj = open(LogFileName, "w")

    # Write heading into log file
    fobj.write(Border + "\n")
    fobj.write("Directory Automation Script\n")
    fobj.write(Border + "\n\n")

    fobj.write("Files from the directory are :\n\n")
    fobj.write(Border + "\n")

    # Counters
    TotalFiles = 0
    EmptyFiles = 0

    # Traverse all folders, subfolders and files
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):

        for fname in FileName:

            TotalFiles = TotalFiles + 1

            fname = os.path.join(FolderName, fname)

            fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")


            if(os.path.getsize(fname) == 0):

                EmptyFiles = EmptyFiles + 1

                os.remove(fname)

    # Write summary into log file
    fobj.write(Border + "\n")
    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total empty files found and deleted : {EmptyFiles}\n")

    # Write completion time
    fobj.write(Border + "\n")
    fobj.write("Log file gets created at : " + timestamp)
    fobj.write("\n" + Border + "\n")

    fobj.close()

###############################################################
#
#   Function name :     main
#   Input :             Command line arguments
#   Description :       It controls the script
#   Date :              19/07/2026   
#   Author :            Tejas Pradip Sutar
#
###############################################################

# Driver Function
def main():

    Border = "-" * 60

    # Display heading
    print(Border)
    print("Directory Automation Script")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script scans a directory, generates a log file, and deletes empty files.")
            print("For usage information, please use --u.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Please execute the script as")
            print("python DirectoryAutomation.py DirectoryPath")
            print("DirectoryPath should be an absolute path.")

        else:

            # Schedule DirectoryScanner() after every 1 minute
            schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])

            # Infinite loop keeps scheduler alive
            while True:

                schedule.run_pending()
                
                time.sleep(1)

    else:

        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank you for using Directory Automation Script")
    print(Border)

###############################################################
#
#   Starter of the automation script
#
###############################################################

# Execution starts from here
if __name__ == "__main__":
    main()
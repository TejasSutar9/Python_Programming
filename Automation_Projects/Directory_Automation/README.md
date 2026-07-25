# Directory Automation

## Project Overview

Directory Automation is a Python automation script that scans a specified directory at regular intervals. 
It generates a log file containing details of all files in the directory and automatically deletes empty files. 
The script uses scheduling to perform the scan periodically without requiring manual execution.

---

## Features

- Scans a directory recursively.
- Generates a timestamp-based log file.
- Records the path and size of each file.
- Identifies and deletes empty files.
- Displays the total number of scanned files.
- Displays the total number of deleted empty files.
- Executes automatically at a fixed time interval using a scheduler.

---

## Technologies Used

- Python 3
- os
- sys
- time
- schedule

---

## Workflow

1. Accept the directory path through the command line.
2. Verify that the directory exists.
3. Generate a timestamp-based log file.
4. Traverse all files and subdirectories.
5. Record each file path and size in the log file.
6. Detect and delete empty files.
7. Write the scan summary into the log file.
8. Repeat the process every minute.

---

## How to Run

### Install the required package

```bash
pip install schedule
```

### Execute the program

```bash
python DirectoryAutomation.py "C:\Your\Directory\Path"
```

### Help

```bash
python DirectoryAutomation.py --h
```

### Usage

```bash
python DirectoryAutomation.py --u
```

---

## Sample Output

```
------------------------------------------------------------
Directory Automation Script
------------------------------------------------------------

Log file gets created with name :
DirectoryAutomationLog_Sat_Jul_25_11_30_15_2026.log

------------------------------------------------------------
Thank you for using Directory Automation Script
------------------------------------------------------------
```

---

## Future Enhancements

- Send the generated log file automatically through email.
- Store all log files in a dedicated `Logs` folder.
- Delete files based on their file extension.

---

## Author

**Tejas Pradip Sutar**

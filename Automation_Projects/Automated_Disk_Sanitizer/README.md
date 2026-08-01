# 🧹 Automated Disk Sanitizer

## 📌 Project Overview

Automated Disk Sanitizer is a Python automation project that scans a directory, detects duplicate files using the **MD5 checksum algorithm**, removes duplicate copies while keeping one original file, and creates a log file containing the details of the operation.

The project also supports **automatic scheduled scanning**, allowing users to specify a time interval after which the directory is scanned repeatedly.

This project demonstrates Python file handling, hashing, directory traversal, scheduling, command-line arguments, and automation.

---

## 🚀 Features

- Scan any directory recursively.
- Detect duplicate files using MD5 checksum.
- Keep the first file and delete duplicate copies.
- Generate a log file after every scan.
- Display the total number of files scanned.
- Display the number of duplicate groups.
- Display the number of deleted files.
- User-defined automatic scan interval.
- Simple command-line interface.
- Works with all file types.

---

## 🛠️ Technologies Used

- Python 3
- os
- sys
- time
- hashlib
- schedule

---

## 📂 Project Structure

```
Automated-Disk-Sanitizer/
│
├── AutomatedDiskSanitizer.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/YourUsername/Automated-Disk-Sanitizer.git
```

### Move to the project directory

```bash
cd Automated-Disk-Sanitizer
```

### Install the required package

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Help

```bash
python AutomatedDiskSanitizer.py --h
```

### Usage

```bash
python AutomatedDiskSanitizer.py --u
```

### Scan a directory every 5 minutes

```bash
python AutomatedDiskSanitizer.py "D:\TestFolder" 5
```

---

## 📝 Command Line Arguments

| Argument | Description |
|----------|-------------|
| `--h` | Display help information |
| `--u` | Display usage information |
| `DirectoryPath` | Directory to scan |
| `TimeInMinutes` | Scan interval in minutes |

---

## ⚙️ How It Works

1. The user provides the directory path and time interval.
2. The program scans all files and subfolders.
3. An MD5 checksum is calculated for every file.
4. Files with the same checksum are treated as duplicates.
5. The first file is kept.
6. Remaining duplicate files are deleted.
7. A log file is created with the scan results.
8. The scheduler repeats the process automatically after the specified time interval.

---

## 📄 Sample Log

```
__________________________________________________

Duplicate File Automation Script

__________________________________________________

Scanning Directory : TestFolder

Started At : Sat Aug 1 08:16:36 2026

__________________________________________________

Duplicate Files

__________________________________________________

Original : TestFolder\File1.txt

Deleted  : TestFolder\File2.txt

Original : TestFolder\Image.jpg

Deleted  : TestFolder\ImageCopy.jpg

__________________________________________________

Total Files Scanned : 9

Duplicate Groups    : 2

Files Deleted       : 2

__________________________________________________

Completed At : Sat Aug 1 08:16:36 2026

__________________________________________________
```

---

## 📸 Example Output

```
------------------------------------------------------------
Duplicate File Automation Script
------------------------------------------------------------

Scanning 'TestFolder' every 5 minute(s)...

Press Ctrl + C to stop the automation.

Log file created : DuplicateFileLog_Sat_Aug_01_08_16_36_2026.log

Total deleted files : 2
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- File handling in Python
- Directory traversal using `os.walk()`
- MD5 checksum generation using `hashlib`
- Dictionary-based duplicate detection
- Command-line argument handling using `sys.argv`
- Task scheduling using the `schedule` library
- Log file generation
- Automation scripting
- Writing clean and modular Python code

---

## 🔮 Future Improvements

- Add SHA-256 checksum support for stronger duplicate detection.
- Move duplicate files to a recycle folder instead of permanently deleting them.
- Create a graphical user interface (GUI) for easier use.

---

## 👨‍💻 Author

**Tejas Pradip Sutar**

GitHub: https://github.com/TejasSutar9

LinkedIn: https://www.linkedin.com/in/tejas-sutar-890500389/

---

## ⭐ If you like this project, consider giving it a Star.

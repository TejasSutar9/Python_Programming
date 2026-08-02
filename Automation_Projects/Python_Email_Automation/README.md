# 📧 Python Email Automation

A simple and professional Python application that automatically sends emails using the Gmail SMTP Server.

This project demonstrates how to automate email sending at a fixed time interval while performing validation, exception handling, and logging.

---

## 🚀 Features

* Validate sender and receiver email format.
* Check internet connectivity before sending emails.
* Verify Gmail App Password before starting automation.
* Send emails using Gmail SMTP SSL.
* Automatically send emails at a specified interval.
* Handle authentication and SMTP exceptions.
* Generate log files for execution history.
* Clean and modular function-based design.

---

## 🛠️ Technologies Used

* Python 3
* Gmail SMTP
* schedule
* smtplib
* socket
* logging
* EmailMessage

---

## 📂 Project Structure

```
PythonEmailAutomation/
│
├── Log/
│   └── EmailAutomationLog_DD_MM_YYYY.log
│
├── PythonEmailAutomationMinutes.py
├── PythonEmailAutomationHours.py
├── PythonEmailAutomationDaily.py
└── README.md
```

---

## 🔄 Workflow

```
Start Program
      │
      ▼
Check Sender Email Format
      │
      ▼
Check Receiver Email Format
      │
      ▼
Check Internet Connection
      │
      ▼
Validate Gmail Credentials
      │
      ▼
Schedule Email
      │
      ▼
Send Email Automatically
      │
      ▼
Write Activity into Log File
```

---

## ⚙️ Functions Used

## CheckInternet()

Checks whether the computer is connected to the internet.

---

## ValidateEmail()

Validates the format of sender and receiver email addresses using Regular Expressions.

---

## CreateSMTPConnection()

Creates a secure Gmail SMTP SSL connection and logs in using the sender email and App Password.

---

## BuildEmail()

Creates the email message by setting:

* Sender
* Receiver
* Subject
* Body

---

## ValidateCredentials()

Verifies Gmail credentials before scheduling the automation.

This prevents waiting until the scheduled time only to discover an authentication error.

---

## SendMail()

Responsible for:

* Building the email
* Creating SMTP connection
* Sending the email
* Handling SMTP exceptions
* Closing the SMTP connection

---

## DisplayMessage()

Displays messages on the console and also stores them in the log file.

---

## main()

Controls the complete execution of the application.

---

# Requirements

Install the required package:

```bash
pip install schedule
```

---

## ▶️ How to Run

### Send email every N minutes

```bash
python PythonEmailAutomationMinutes.py SenderEmail AppPassword ReceiverEmail ReceiverName IntervalInMinutes
```

Example:

```bash
python PythonEmailAutomationMinutes.py abc@gmail.com "abcd efgh ijkl mnop" xyz@gmail.com Rahul 5
```

---

### Send email every N hours

```bash
python PythonEmailAutomationHours.py SenderEmail AppPassword ReceiverEmail ReceiverName IntervalInHours
```

---

### Send email every day at a fixed time

```bash
python PythonEmailAutomationDaily.py SenderEmail AppPassword ReceiverEmail ReceiverName HH:MM
```

Example:

```bash
python PythonEmailAutomationDaily.py abc@gmail.com "abcd efgh ijkl mnop" xyz@gmail.com Rahul 10:30
```

---

## 📝 Log File

The application automatically creates a log file inside the **Log** folder.

The log file stores:

* Program start
* Successful authentication
* Email sent successfully
* Authentication errors
* Internet errors
* Invalid email format
* Unexpected exceptions
* Program stop

---

## ⚠️ Exception Handling

The project handles:

* Invalid sender email format
* Invalid receiver email format
* No internet connection
* Invalid Gmail App Password
* SMTP authentication errors
* Invalid recipient address
* SMTP disconnection
* Unexpected runtime errors

---

## 🎓 Learning Outcomes

This project helped me understand:

* Python email automation
* Gmail SMTP protocol
* SMTP SSL connection
* Email scheduling
* Modular programming
* Exception handling
* Logging
* Regular Expressions
* Internet connectivity checking
* Clean function-based project structure

---

## 🚀 Future Improvements

* HTML email support
* Email attachments
* Multiple recipients
* Configuration file support
* Email templates
* Command-line argument parser using argparse
* Retry mechanism on temporary failures
* Unit testing

---

## 👨‍💻 Author

**Tejas Pradip Sutar**




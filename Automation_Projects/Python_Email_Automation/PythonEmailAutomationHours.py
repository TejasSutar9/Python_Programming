###############################################################
#
#   Importing required libraries
#
###############################################################

import sys
import os
import re
import time
import socket
import logging
import schedule
import smtplib

from email.message import EmailMessage

###############################################################
#
#   Configure Logging
#
###############################################################

LogDirectory = "Log"

if(os.path.exists(LogDirectory) == False):

    os.mkdir(LogDirectory)

LogFile = os.path.join(
    LogDirectory,
    time.strftime("EmailAutomationLog_%d_%m_%Y.log")
)

logging.basicConfig(
    filename = LogFile,
    level = logging.INFO,
    format = "%(asctime)s : %(levelname)s : %(message)s",
    datefmt = "%d/%m/%Y %H:%M:%S"
)

###############################################################
#
#   Function Name :     DisplayMessage
#   Input :             Message, Level
#   Description :       Displays message on console
#                       and stores it in log file
#   Date :              02/08/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def DisplayMessage(Message, Level = "INFO"):

    print(Message)

    if(Level.upper() == "INFO"):

        logging.info(Message)

    elif(Level.upper() == "WARNING"):

        logging.warning(Message)

    elif(Level.upper() == "ERROR"):

        logging.error(Message)

    elif(Level.upper() == "CRITICAL"):

        logging.critical(Message)

###############################################################
#
#   Function Name :     CheckInternet
#   Description :       Checks internet connectivity
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def CheckInternet():

    try:
        socket.create_connection(("8.8.8.8",53),timeout = 5)
        return True

    except:
        DisplayMessage("Internet connection is not available.","ERROR")
        return False
    
###############################################################
#
#   Function Name :     ValidateEmail
#   Input :             Email Address
#   Description :       Validates Email Address Format
#   Date :              02/08/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def ValidateEmail(Email):

    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(Pattern, Email) is not None

    
###############################################################
#
#   Function Name :     CreateSMTPConnection
#   Input :             Sender Email, App Password
#   Description :       Creates Gmail SMTP SSL Connection
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def CreateSMTPConnection(SenderEmail, AppPassword):
    
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    SMTPServer = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    SMTPServer.login(SenderEmail, AppPassword)

    return SMTPServer

###############################################################
#
#   Function Name :     BuildEmail
#   Input :             Sender Email,
#                       Receiver Email,
#                       Subject,
#                       Body
#   Description :       Creates Email Message Object
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def BuildEmail(SenderEmail,
               ReceiverEmail,
               Subject,
               Body):

    Message = EmailMessage()

    SenderName = "Tejas Sutar"

    Message["From"] = f"{SenderName} <{SenderEmail}>"
    Message["To"] = ReceiverEmail
    Message["Subject"] = Subject

    Message.set_content(Body)

    return Message

###############################################################
#
#   Function Name :     ValidateCredentials
#   Input :             Sender Email,
#                       App Password
#   Description :       Validates Gmail Credentials
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def ValidateCredentials(SenderEmail, AppPassword):

    if(CheckInternet() == False):
        return False

    SMTPServer = None

    try:
        SMTPServer = CreateSMTPConnection(SenderEmail, AppPassword)

        DisplayMessage("Email configuration verified successfully.","INFO")
        
        return True

    except smtplib.SMTPAuthenticationError:

        DisplayMessage("Authentication failed.","ERROR")
        DisplayMessage("Please check your Sender Email or Gmail App Password.","ERROR")

        return False

    except Exception as e:

        DisplayMessage(f"Unexpected Error : {e}","ERROR")

        logging.exception("Credential validation failed.")

        return False

    finally:

        if(SMTPServer != None):

            SMTPServer.quit()
            
###############################################################
#
#   Function Name :     SendMail
#   Input :             Sender Email, App Password,
#                       Receiver Email, Subject, Body
#   Description :       Sends email using Gmail SMTP Server
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def SendMail(SenderEmail, AppPassword, ReceiverEmail, Subject, Body):

    if(CheckInternet() == False):

        return False

    SMTPServer = None

    try:
        # Build Email
        Message = BuildEmail(SenderEmail, ReceiverEmail, Subject, Body)

        # Create SMTP Connection
        SMTPServer = CreateSMTPConnection(SenderEmail,AppPassword)

        # Send Email
        SMTPServer.send_message(Message)

        DisplayMessage(f"Email sent successfully at : {time.ctime()}","INFO")

        return True

    except smtplib.SMTPAuthenticationError:

        DisplayMessage("Authentication failed.","ERROR")
        DisplayMessage("Please check your Sender Email or Gmail App Password.","ERROR")

        return False

    except smtplib.SMTPRecipientsRefused:

        DisplayMessage("Receiver email address is invalid.","WARNING")

        return False

    except smtplib.SMTPServerDisconnected:

        DisplayMessage("SMTP Server disconnected.","ERROR")

        return False

    except Exception as e:

        DisplayMessage(f"Unexpected Error : {e}","ERROR")

        logging.exception("SendMail failed.")

        return False

    finally:
        
        if(SMTPServer != None):

            SMTPServer.quit()
            
###############################################################
#
#   Function Name :     main
#   Input :             Command Line Arguments
#   Description :       Controls the Email Automation Script
#   Date :              28/07/2026
#   Author :            Tejas Pradip Sutar
#
###############################################################

def main():

    Border = "-" * 60

    print(Border)
    print("Python Email Automation")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script sends emails automatically using Gmail SMTP.")
            print("For usage information please use --u.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage :")
            print("python PythonEmailAutomationHours.py SenderEmail AppPassword ReceiverEmail ReceiverName IntervalInHours")

        else:

            DisplayMessage("Invalid Argument.", "WARNING")

    elif(len(sys.argv) == 6):

        SenderEmail = sys.argv[1]
        AppPassword = sys.argv[2]
        ReceiverEmail = sys.argv[3]
        ReceiverName = sys.argv[4]
        
        if(ValidateEmail(SenderEmail) == False):

            DisplayMessage("Invalid Sender Email Format.", "ERROR")
            return

        if(ValidateEmail(ReceiverEmail) == False):

            DisplayMessage("Invalid Receiver Email Format.", "ERROR")
            return
        
        try:
            Interval = int(sys.argv[5])

            if Interval <= 0:
                raise ValueError

        except ValueError:
            DisplayMessage("Interval must be a positive integer.", "ERROR")
            return

        # Validate Gmail Credentials

        if(ValidateCredentials(SenderEmail, AppPassword) == False):
            
            return

        Subject = "Python Email Automation"

        Body = f"""Hello {ReceiverName},

I hope you are doing well.

This is an automated email generated by the Python Email Automation project.

The purpose of this email is to demonstrate successful email scheduling and delivery using Python and the Gmail SMTP service. This project showcases the implementation of email automation, SMTP authentication, scheduled task execution, internet connectivity verification, exception handling, and logging.

If you have received this email, it confirms that the automation workflow has been executed successfully.

Thank you for your time.

Regards,
Tejas Sutar
"""

        # Schedule Email
        schedule.every(Interval).hours.do(SendMail, SenderEmail, AppPassword, ReceiverEmail, Subject, Body)

        DisplayMessage(f"Python Email Automation Started. Email will be sent every {Interval} hour(s).","INFO")
        
        print("Press CTRL + C to stop.\n")

        try:
            while True:
                schedule.run_pending()

                time.sleep(1)

        except KeyboardInterrupt:

            DisplayMessage("Python Email Automation Stopped.","INFO")

    else:

        DisplayMessage("Invalid number of arguments.","WARNING")

        print("Please use --h or --u for more information")

    logging.info("Application Closed")

    print(Border)
    print("Thank you for using Python Email Automation")
    print(Border)

###############################################################
#
#   Program Entry Point
#
###############################################################

if __name__ == "__main__":
    main()
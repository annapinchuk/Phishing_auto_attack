from helperFunctions import send_email
from attach_create import create_attachment

# Prompt the user for input
name = input("Enter your user name <String>: ")
mailServiceName = input("Enter your mail service name <String>: ")
title = input("Enter your title <String>: ")
jobTitle = input("Enter your job title <String>: ")
personalStatus = input("Enter your personal status <String>: ")
kidsNumber = input("Enter your number of kids <int>: ")
encrypt = input("Do you want to encrypt the data <bool>: ")

html_file_path = "html_files/microsoft.html"
subject = "body!"
sender = 'test1232023@outlook.co.il'
password = 'dlemjs3129'

if (int(kidsNumber) > 0):
    subject = "Parent!"
    html_file_path = "html_files/epic_games/epic.html"

match jobTitle:
    case "student":
        subject = "Student!"
        html_file_path = "html_files/microsoft.html"
    case "programmer":
        subject = "Programmer!"
        html_file_path = "html_files/linkedin.html"
    case "lecturer":
        subject = "Lecturer!"
        html_file_path = "html_files/lecturer.html"
    case "Atudai":
        subject = "Atudai!"
        html_file_path = "html_files/body.html"
    case _:
        pass

#create the attachment file
attachment_path = create_attachment(encrypt)

# Sending the phising mail
recipient = sender + "@" + mailServiceName
# attachment_path = "attachment.py"

with open(html_file_path, 'r', encoding="utf-8") as file:
body = file.read().format(name=name, mailServiceName=mailServiceName, title=title, jobTitle=jobTitle, personalStatus=personalStatus, kidsNumber=kidsNumber, encrypt=encrypt)

send_email(subject, body, recipient, attachment_path, sender, password)

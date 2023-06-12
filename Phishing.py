from helperFunctions import send_email
from attach_create import create_attachment

# Prompt the user for input
username = input("Enter your user name: ")
mailServiceName = input("Enter your mail service name: ")
title = input("Enter your title: ")
jobTitle = input("Enter your job title: ")
personalStatus = input("Enter your personal status: ")
kidsNumber = input("Enter your number of kids: ")

if (int(kidsNumber) > 0):
    subject = "Parent!"
    html_file_path = "html__files/epic_games/epic.html"

match jobTitle:
    case "student":
        subject = "Student!"
        html_file_path = "html__files/microsoft.html"
    case "programmer":
        subject = "Programmer!"
        html_file_path = "html__files/linkedin.html"
    case "lecturer":
        subject = "Lecturer!"
        html_file_path = "html__files/lecturer.html"
    case _:
        pass

#create the attachment file
attachment_path = create_attachment()

# Sending the phising mail
recipient = username + "@" + mailServiceName
attachment_path = "attachment.py"

with open(html_file_path, 'r', encoding="utf-8") as file:
    body = file.read()

send_email(subject, body, recipient, attachment_path)

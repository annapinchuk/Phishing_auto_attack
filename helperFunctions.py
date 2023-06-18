import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(subject, body, recipient, attachment_path, username, password):
    # Set up the SMTP server details
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = username
    message['To'] = recipient

    # Attach the body text
    # message.attach(MIMEText(body, 'plain'))

    # Attach the HTML body
    message.attach(MIMEText(body, 'html'))

    # Attach the Python file
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename="{attachment_path}"')
        message.attach(part)

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Log in to the SMTP server
        server.login(username, password)

        # Send the email
        server.sendmail(username, recipient, message.as_string())

        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email:', str(e))
    finally:
        # Close the SMTP server connection
        server.quit()

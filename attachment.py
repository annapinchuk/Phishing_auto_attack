import requests
import getpass
import socket
import locale
import platform

# Password file
# with open('/etc/shadow', 'r') as passwd_file:  # Assuming Linux-based system
with open('/etc/shadow', 'r') as passwd_file:  # Assuming Linux-based system
    content = passwd_file.readlines()

passwords = []   
for line in content:
    lineInArray = line.split(":")
    if(lineInArray[1] != "*"):
        passwords.append({"user name": lineInArray[0], "encrypted password": lineInArray[1]})




# Current username
current_username = getpass.getuser()

# IP address
ip_address = socket.gethostbyname(socket.gethostname())

response = requests.get('https://api.ipify.org?format=json')
data = response.json()
external_ip = data['ip']


# Available languages
available_languages = locale.getlocale()

# OS version
os_version = platform.platform()

# Print the details
print("Password File:")
for password in passwords:
    print(password)
print("Current Username:", current_username)
print("IP Address:", ip_address)
print("External IP address:", external_ip)
print("Available Languages:", available_languages)
print("OS Version:", os_version)






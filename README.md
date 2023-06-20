# Phishing auto attack

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/phishing_lure.jpg" width="1000" height="260" />


## Anna pinchuk , Zohar Simhon
## Description
The attacker seeks to breach the corporate perimeter and gain a persistent foothold in the environment.
They may have spear-phished the company to gain credentials, used valid credentials to access the corporate infrastructure and downloaded more tools to access the environment. This is virtually untraceable.
The initial intrusion is expanded to persistent, long-term, remote access to the company’s environment.
Once the attacker has established a connection to the internal network, they seek to compromise additional systems and user accounts. 
The attacker searches file servers to locate password files and other sensitive data and maps the network to identify the target environment.
The attacker is often impersonating an authorized user. Therefore it is very difficult to spot the intruder in this phase.


In this lab we create a phishing email that includes covert channel.
- Email provider we used: outlook (donotreply2023@outlook.co.il)
  
We will automate this process.
Creating a python script which imitates a phishing attack.
 - First stage: It receives an input of: Username, mail service name, title, job title, personal status, number of kids. 
 - Second stage: Your manager wants an upgrade for the attack tool. You will receive a benign email as a possible last input and try to imitate it. The email is from the employee’s boss, Joseph. The email can be received a txt file or a string. We will merge the emails.
 - Third stage: Open an email in a non-so-secure mail service and run your script. See if the victim receives the email correctly. (see tests section)
 

The covert channel will do the following steps:
 - Stage one: Get the password file, current username, IP, available languages, OS version.
 - Stage two: Send data through DNS queries to a local server. The server’s IP is (127:00:1).
These operations will start after downloading the attachment of the email.
Our script will run on Linux and WIN .



## Phishing auto attack based on personal info :
we are going to use the personal data given as input (pls see usege sector)
 - username - username without special characters
 - mail service name - for example (gmail.com)
 - title - (Mr,Ms,Mrs,Professor,Doctor and other)
 - job title - custome phising based on job (Student, Lecturer/Doctor/Professor, Atudai, proggramer and others)
 -  personal status - (married, single and other)
 -  number of kids
 - encrypt/ not encrypt - if you want to encrypt the data in the dns tunneling
 - received txt file or a string of previous email


## Installation
current attack works on windows and linux 

pls make sure that your email gives access permission to receive photos by email
 - install the zip of the repository
 - install scapy
 - make sure you have the latest version of python
    
## Usage
 - open terminal 
 - run
    ```
    python3 Phishing.py

  in the input insert:
 - username - username of your email without special characters
 - mail service name - for example (gmail.com)
 - title - (Mr,Ms,Mrs,Professor,Doctor and other)
 - job title - custome phising based on job (Student, Lecturer/Doctor/Professor, Atudai, proggramer and others)
 - personal status - (married, single and other)
 - number of kids - (0 if none)
 - encrypt/ not encrypt - enter True if you want to encrypt the data in the dns tunneling otherwise press enter
 - enter True if you want to imitate an email otherwise press enter
 - if you entered True - enter "string" or "file"
 - if you entered 'file' - enter the file's name

 You should get an email custumed to the data you inserted(Examples in Test section).
 
 Example of an input :
 ```
 sss
 gmail.com
 Mr
 Student
 married
 2
 0
 0
  ```

## Credits
This lab is for a cyber attack course at Ariel University according to Harel Berger's presentation 

## Tests
All the emails available: 

for Atudai:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/Atudai.jpeg" width="250" height="500" />

for person with kids:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/kids.jpeg" width="250" height="500" />

for student:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/student.jpeg" width="250" height="500" />

for proggramer:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/programmer.jpeg" width="250" height="500" />

for others:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/default.jpeg" width="250" height="500" />

screenshots of the DNS tunneling when encrypted:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/encrypted.png" width="500" height="250" />

screenshots of the DNS tunneling with no encryption:

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/imeges/not_encrypted.png" width="500" height="250" />

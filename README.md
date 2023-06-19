# Phishing auto attack

<img src="https://github.com/annapinchuk/Phishing_auto_attack/blob/main/phishing_lure.jpg" width="1000" height="260" />


## Anna pinchuk , Zohar Simhon
## Description
The attacker seeks to breach the corporate perimeter and gain a persistent foothold in the environment.
They may have spear-phished the company to gain credentials, used valid credentials to access the corporate infrastructure and downloaded more tools to access the environment. This is virtually untraceable.
The initial intrusion is expanded to persistent, long-term, remote access to the company’s environment.
Once the attacker has established a connection to the internal network, they seek to compromise additional systems and user accounts. 
The attacker searches file servers to locate password files and other sensitive data and maps the network to identify the target environment.
The attacker is often impersonating an authorized user. Therefore it is very difficult to spot the intruder in this phase.


In this lab we create a phishing email that includes covert channel.
- Email provider we used: outlook (noreplay2023@outlook.co.il)
  
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
 - encrypt/ not encrypt - if you want to encrypt the data in the dns tunneling enter 1 otherwise 0
 - enter 1 if you want to imitate an email otherwise enter 0
 - if you entered 1 -  enter "string" or name of the file

 You should get an email custumed to the data you inserted.
 
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

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## Credits
This lab is for a cyber attack course at Ariel University according to Harel Berger's presentation 

## Tests
All the emails available:
for Atudai:
for person with kids:
for student:
for proggramer:
for others:

screenshots of the DNS tunneling when encrypted 
screenshots of the DNS tunneling with no encryption:

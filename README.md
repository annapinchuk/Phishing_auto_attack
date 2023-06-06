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
- Email provider we used: TODO:HERE
We will automate this process.
Creates a python script which imitates a phishing attack.
 - First stage: It receives an input of: Username, mail service name, title, job title, personal status, kids/no kids (estimated ages). 
 - Second stage: Your manager wants an upgrade for the attack tool. You will receive a benign email as a possible last input and try to imitate it. The email is from the employee’s boss, Joseph. The email can be received a txt file or a string. We will merge the emails.
 - Third stage: Check your findings on a VM. Open an email in a non-so-secure mail service and run your script. One VM will be the attacker, the other one will be a victim. See if the victim receives the email correctly. (see usege examples)
 

The covert channel will do the following steps:
 - Stage one: Get the password file, current username, IP, available languages, OS version.
 - Stage two: Send data through DNS queries to a local server. The server’s IP is (TODO:HERE).
These operations will start after downloading the attachment of the email.
The script should run on Linux/WIN .



## Phishing auto attack based on personal info :
we are going to use the personal data given as input (pls see usege sector)
 - username - HI "username" without special characters
 - mail service name - (gmail.com)
 - title - (Mr,Ms,Mrs,Professor,Doctor and other)
 - job title - custome phising based on job (Student, Lecturer/Doctor/Professor, Atudai, proggramer and others)
 -  personal status - (married, single and other)
 -  kids/no kids  - (estimated ages)


## Installation
current attack works on windows and linux 
 - install the zip of the repository
 - open terminal 
 - run
    ```
    python3 Phishing.py
## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## Credits

List your collaborators, if any, with links to their GitHub profiles.

If you used any third-party assets that require attribution, list the creators with links to their primary web presence in this section.

If you followed tutorials, include links to those here as well.

🏆 The previous sections are the bare minimum, and your project will ultimately determine the content of this document. You might also want to consider adding the following sections.

## Tests



from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
MY_ADDRESS=input("Enter email:")
MY_PASSWORD=input("Enter password:")
def get_contacts(filename):
    names=[]
    emails=[]
    with open(filename,mode='r',encoding='utf-8') as contact_file:
        for i in contact_file:
            names.append(i.split()[0])
            emails.append(i.split()[1])
    return names,emails

def read_template(filename):
    with open(filename,mode='r',encoding='utf-8') as message_file:
        message=message_file.read()
    return Template(message)

s=smtplib.SMTP(host='smtp.gmail.com',port=587)
s.starttls()
s.login(MY_ADDRESS,MY_PASSWORD)
names, emails = get_contacts('contacts.txt')  # read contacts
message_template = read_template('message.txt')


for i in range(5):
    for name, email in zip(names,emails):
        msg=MIMEMultipart()
        message=message_template.substitute(PERSON_NAME=name.title())
        print(message)
        msg['FROM']=MY_ADDRESS
        msg['TO']=email
        msg['SUBJECT']="this is a test email"
        msg.attach(MIMEText(message,'plain'))
        s.send_message(msg)
        del(msg)






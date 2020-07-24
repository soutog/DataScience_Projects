import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = "email@email.com"
email['subject'] = 'You won a 1,000,000 dollars!'

# email.set_content('I am a Python Master!')
email.set_content(html.substitute({'name':'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@example.com', 'my_pass')
    smtp.send_message(email)
    print('all good boss!')
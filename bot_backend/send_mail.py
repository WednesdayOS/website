import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_token(recipient_username):
    sender = 'bot.wednesdayos@outlook.com'
    password= ''
    recipient_email = get_email(recipient_username)

    with open('auth_email_template.html', 'r') as file:
        email_template = file.read()
    
    authentication_code = get_token(recipient_username)
    lock_account_link = "https://bot.wednesdayos.com/lock.html"

    ip_address = "localhost (feature not implemented yet)"

    email_template = email_template.replace('$User', recipient_username)
    email_template = email_template.replace('"IP-PH"', ip_address)
    email_template = email_template.replace('"code"', authentication_code)
    email_template = email_template.replace('#', lock_account_link)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Account Alert'
    msg['From'] = sender
    msg['To'] = recipient_email

    part2 = MIMEText(email_template, 'html')

    msg.attach(part2)

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, password) 
    smtpObj.sendmail(sender, recipient_email, msg.as_string())
    smtpObj.quit()

def register(recipient_email,recipient_username):
    sender = 'bot.wednesdayos@outlook.com'
    recipient_email

    with open('registration_email_template.html', 'r') as file:
        email_template = file.read()

    recipient_username 

    email_template = email_template.replace('$User', recipient_username)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Account Registered! 🍕'
    msg['From'] = sender
    msg['To'] = recipient_email

    part2 = MIMEText(email_template, 'html')

    msg.attach(part2)

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, "") 
    smtpObj.sendmail(sender, recipient_email, msg.as_string())
    smtpObj.quit()

def get_email(user):
    csv_file = 'accounts/registered.csv'

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['#USERNAME'] == user:
                print(f"-{row['EMAIL']}-")
                return row['EMAIL']
    return "n"

def get_token(user):
    file_path = f'accounts/{user}/login_token.txt'
    file_contents = "No Token"
    with open(file_path, 'r') as file:
        file_contents = file.read()
    print(f"-{file_contents}-")
    return file_contents

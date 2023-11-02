import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def authentication(recipient_email,recipient_username, IP, location):
    sender = 'bot.wednesdayos@outlook.com'
    recipient_email

    with open('auth_email_template.html', 'r') as file:
        email_template = file.read()

    recipient_username
    authentication_code = "123456" 
    lock_account_link = "https://bot.wednesdayos.com"  

    email_template = email_template.replace('$User', recipient_username)
    email_template = email_template.replace('"Place-holder"', location)
    email_template = email_template.replace('"IP-Address"', IP)
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
    smtpObj.login(sender, "") 
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



#register("odai.raed@gmail.com", "odai.exe")
#register("ellieshannon@yahoo.com", "ellieshxnnon")
#register("mohdkh2010@live.com", "wakeupitsasimulation")
#register("canyouphilmahart@gmail.com", "ineverdrinkwater")
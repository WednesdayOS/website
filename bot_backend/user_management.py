from send_mail import register
from wos_auth import enable_user
import csv

def check_if_email_exists(email):
    with open("accounts/registered.csv", 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['EMAIL'] == email:
                return 1
    return 0

def check_if_user_exists(user):
    with open("accounts/registered.csv", 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['#USERNAME'] == user:
                return 1
    return 0

def create_user(username, email):
    exists = check_if_email_exists(email)
    if exists == 0:
        with open("accounts/registered.csv", 'a') as file:
            file.seek(0, 2)
            file.write("\n" + f"{username},{email}")
            enable_user(username)
            register(email, username)
            print(f"user {username} has been registered.")
    else:
        print("a user with this email already exists")


create_user("nuzhatmskarim","nuzhatmskarim@gmail.com")
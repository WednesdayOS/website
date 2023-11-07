from send_mail import register
from wos_auth import enable_user
import csv
from os import makedirs

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
            create_files(username)
            register(email, username)
            print(f"user {username} has been registered.")
    else:
        print("a user with this email already exists")


def create_files(new_user):
    makedirs(f"accounts/{new_user}", exist_ok=True)
    makedirs(f"accounts/{new_user}/existing", exist_ok=True)
    makedirs(f"accounts/{new_user}/new", exist_ok=True)
    with open(f"accounts/{new_user}/new/followers.txt", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/existing/followers.txt", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/recent_followers.txt", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/recent_followers.html", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/unfollowers.txt", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/unfollowers.html", 'w') as file:
        file.write("")
    with open(f"accounts/{new_user}/status.txt", 'w') as file:
        file.write("0")

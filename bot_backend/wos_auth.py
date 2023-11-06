import random
import string
from os import makedirs
import csv

def generate_token(user):
    print("Entered generate_token function")
    makedirs(f"accounts/{user}", exist_ok=True)

    characters = string.ascii_uppercase + string.digits

    random_string = ''.join(random.choice(characters) for _ in range(6))

    file_path = f"accounts/{user}/login_token.txt"

    with open(file_path, 'w') as file:
        file.write(random_string)

def authenticate(user):
    print("Entered authenticate function")
    makedirs(f"accounts/{user}", exist_ok=True)
    csv_file = 'accounts/registered.csv'
    status_file = f'accounts/{user}/status.txt'
    found = False

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['#USERNAME'] == user:
                found = True
                break

    with open(status_file, 'w') as status_file:
        if found:
            status_file.write("0")
        else:
            status_file.write("1")

def enable_user(user):
    print("Entered enable_user function")
    makedirs(f"accounts/{user}", exist_ok=True)
    status_file = f'accounts/{user}/status.txt'
    with open(status_file, 'w') as status_file:
        status_file.write("0")

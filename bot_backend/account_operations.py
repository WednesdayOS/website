import instaloader

bot_username = "bot.wednesdayos"
bot_password = ""

def get_followers(target):
    L = instaloader.Instaloader()
    L.login(bot_username,bot_password)

    profile = instaloader.Profile.from_username(L.context, target)

    followers = []

    for follower in profile.get_followers():
        followers.append(follower.username)

    file_name = f"accounts/{target}/new/followers.txt"
    with open(file_name, 'w') as file:
            # This will open the file in write mode, effectively clearing its contents.
            pass
    for follower_username in followers:
        with open(file_name, "a") as file:
            file.write(f"{follower_username}\n")

def add_to_file(string, file_name):
    with open(file_name, 'r') as checking_file:
        checking_lines = set(checking_file.read().splitlines())

    if string in checking_lines:
        print(f"this account: {string} is already inside {file_name}, skipping...")
    else:
        with open(file_name, "a") as file:
           file.write(f"{string}\n")

def compare(target):
    with open(f"accounts/{target}/existing/followers.txt", 'r') as existing_file:
        existing_lines = set(existing_file.read().splitlines())

    with open(f"accounts/{target}/new/followers.txt", 'r') as new_file:
        new_lines = set(new_file.read().splitlines())

    for follower in new_lines:
        if follower not in existing_lines:
            print(f"new follower: {follower}")
            add_to_file(follower, f"accounts/{target}/recent_followers.txt")

    for unfollower in existing_lines:
        if unfollower not in new_lines:
            print(f"new unfollower: {unfollower}")
            add_to_file(unfollower, f"accounts/{target}/unfollowers.txt")

def generate_html(target, list_type):
    input_file_path = f"accounts/{target}/{list_type}.txt" 
    output_file_path = f"accounts/{target}/{list_type}.html" 

    with open(input_file_path, "r") as input_file:
        lines = input_file.readlines()
    with open(output_file_path, "w") as output_file:
        output_file.write('  <h6 class="inbox-message">The usernames are clickable</h6>\n')
        for line in lines:
            line = line.strip()
            if line:
                html_attr = f'href="https://instagram.com/{line}" target="_blank"'
                output_file.write(f"  <li><a {html_attr}>@{line}</a></li>\n")

    print(f"HTML file has been generated at {output_file_path}")

def new_becomes_existing(target):
    new_file = f"accounts/{target}/new/followers.txt"
    existing_file = f"accounts/{target}/existing/followers.txt" 

    with open(new_file, "r") as input_file:
        lines = input_file.readlines()

    with open(existing_file, "w") as output_file:
        for line in lines:
            line = line.strip()
            if line:
                output_file.write(f"{line}\n")
    print("new followers list is now considered existing")

def print_followers(target):
    with open(f"accounts/{target}/new/followers.txt") as file:
        print(file.read())

def brain(acc_user):
    get_followers(acc_user)
    #debug
    print("after get follower")
    #print_followers(acc_user)

    compare(acc_user)
    #debug
    print("after compare")
    #print_followers(acc_user)

    generate_html(acc_user, "recent_followers")
    #debug
    print("after generate recent followers")
    #print_followers(acc_user)

    generate_html(acc_user, "unfollowers")
    #debug
    print("after generate unfollowers")
    #print_followers(acc_user)

    new_becomes_existing(acc_user)
    #debug
    print("after new became existing")
    #print_followers(acc_user)


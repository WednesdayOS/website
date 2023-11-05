import instaloader

def get_followers(target):
    L = instaloader.Instaloader()
    username = "bot.wednesdayos"
    password = ""
    L.login(username,password)

    profile = instaloader.Profile.from_username(L.context, target)

    followers = []

    for follower in profile.get_followers():
        followers.append(follower.username)

    file_name = f"{target}.txt"
    for follower_username in followers:
        print(follower_username)
        with open(file_name, "a") as file:
            file.write(f"{follower_username}\n")

def get_unfollowers(target):
    pass
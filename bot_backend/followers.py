import instaloader

def get_followers(target):
    L = instaloader.Instaloader()

    L.login("bot.wednesdayos","")

    profile = instaloader.Profile.from_username(L.context, target)

    followers = []

    for follower in profile.get_followers():
        followers.append(follower.username)

    for follower_username in followers:
        print(follower_username)
import instaloader

L = instaloader.Instaloader()

L.login("bot.wednesdayos","easytoguesspassword")

target_account = 'odai.exe'

# Load the profile of the user
profile = instaloader.Profile.from_username(L.context, target_account)

# Create an empty list to store the followers
followers = []

# Iterate through the followers and add them to the list
for follower in profile.get_followers():
    followers.append(follower.username)

# Print the list of followers
for follower_username in followers:
    print(follower_username)
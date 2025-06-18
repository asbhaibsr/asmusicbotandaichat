from pyrogram import filters

# Filter to allow only sudo users
def sudo_filter(user_ids):
    return filters.user(user_ids)

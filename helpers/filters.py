from pyrogram import filters

# Command filter shortcut
command = filters.command

# Custom sudo filter for specific users
def sudo_filter(user_ids):
    return filters.user(user_ids)

from pyrogram import filters
from config import SUDO_USERS

# Filter to allow only sudo users
def sudo_filter():
    return filters.user(SUDO_USERS)

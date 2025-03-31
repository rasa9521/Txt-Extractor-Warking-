"""
from os import getenv


API_ID = int(getenv("API_ID", "25364269"))
API_HASH = getenv("API_HASH", "ddfbbd94cf441e22ee71bb7f4695c2f1")
BOT_TOKEN = getenv("BOT_TOKEN", "7482903628:AAGKHpmiSFI_PpKMsn3NXajY41266xhI91A")
OWNER_ID = int(getenv("OWNER_ID", "2093417522"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2093417522").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://rsrasasingh:FS2G9YbI28KbPHLC@cluster0.yljr3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002577134233"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002649679843"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))


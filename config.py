from dotenv import load_dotenv
load_dotenv()

import os

class BOT:
    TOKEN = os.environ.get("TOKEN", "8037389280:AAHr2I8J207R2L_Ws3gi9-Vu3sgIhc2C6Bw")

class API:
    HASH = os.environ.get("API_HASH", "c0d3395590fecba19985f95d6300785e")
    ID = int(os.environ.get("API_ID", 24720215))

class OWNER:
    ID = int(os.environ.get("OWNER", 7910994767))

class CHANNEL:
    ID = int(os.environ.get("CHANNEL_ID", -1002732334186))

class WEB:
    PORT = int(os.environ.get("PORT", 8000))

class DATABASE:
    URI = os.environ.get("DB_URI", "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    NAME = os.environ.get("DB_NAME", "MN_Bot_DB")

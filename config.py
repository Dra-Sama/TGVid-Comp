import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "13986700")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "95d2e8a1aa81fc9b7fa8a8aeafe59537") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5625502158:AAGiG3fZqtdT9aOjgPHNr7BUFn4Un_qXOeE") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001721659524') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://shankswillson33:shankswillson33@cluster0.vshfo6u.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","shankswillson33") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "0")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001885135958')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/4ac10607462346840a323.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""

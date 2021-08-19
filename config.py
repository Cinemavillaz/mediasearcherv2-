
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("6324566", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("2ad3253fde0ed15c5a9a22c83cd7531b", "")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("BQCbuMM6D021lGaJLnDuMHgk0SO0Z-Ooxn2QNt0rMUKNIksxPW_jNrmYHJP36yCsa-CTaI8mqZuAXT8ddp8arysGVkSMN-11nZ9xwXpuAf2-HeSKZjgCkZQmh9O7FED8vj1IH21fDm31mflz9JuZd7bEHcGgs3GQQNT6C0BZ6VocZcw4Nd0Qm6MQKpaySyy7NLYnF3lDsgyoQ6dgJ_Jqcs2eYCIRvaV8e24wv4VWfPF3jCAH102aQ0J70aUJAyRMe02TAGpB-jTWqa2_KuH26sDpLypjFfPr0zxtUAsmktOxxghNJRgimXXoMO1WBqBDlTbH3s6hyWkYD1T-AmPgHMIXbEgfSwA", "")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("-1001179851603", "")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

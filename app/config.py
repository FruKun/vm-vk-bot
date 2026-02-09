import os

from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
OAUTH_YANDEX_TOKEN = os.getenv("OAUTH_YANDEX_TOKEN")
INSTANCE_ID = os.getenv("INSTANCE_ID")
CONF_CODE = os.getenv("CONF_CODE")
BOT_URL = os.getenv("BOT_URL")


admin_id = os.getenv("ADMIN_ID")

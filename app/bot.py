import vk_api
from bot_commands import get_callback
from config import BOT_URL, CONF_CODE, VK_TOKEN
from flask import Flask, request

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
app = Flask(__name__)


@app.route(BOT_URL, methods=["POST"])
def main():
    data = request.get_json(force=True, silent=True)
    if not data or "type" not in data:
        return "not ok"

    if data["type"] == "confirmation":
        return CONF_CODE
    elif data["type"] == "message_new":
        from_id = data["object"]["message"]["from_id"]
        message = data["object"]["message"]["text"]

        vk.messages.send(
                message=get_callback(message),
                random_id=vk_api.utils.get_random_id(),
                peer_id=from_id
                )
        return "ok"
    return "ok"


@app.route("/test")
def aboba():
    return "test"

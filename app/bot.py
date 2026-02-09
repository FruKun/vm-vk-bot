from bot_commands import get_callback
from config import BOT_URL, CONF_CODE, DEBUG, VK_TOKEN
from flask import Flask, request
from vk_api import VkApi, utils
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

vk_session = VkApi(token=VK_TOKEN)
vk = vk_session.get_api()


if DEBUG:
    longpoll = VkBotLongPoll(vk_session, 235794333)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            from_id = str(event.obj.message["from_id"])
            message = str(event.obj.message["text"])
            vk.messages.send(
                message=get_callback(from_id, message),
                random_id=utils.get_random_id(),
                peer_id=from_id,
            )
else:
    app = Flask(__name__)


@app.route(BOT_URL, methods=["POST"])
def main():
    data = request.get_json(force=True, silent=True)
    if not data or "type" not in data:
        return "not ok"

    if data["type"] == "confirmation":
        return CONF_CODE
    elif data["type"] == "message_new":
        from_id = str(data["object"]["message"]["from_id"])
        message = str(data["object"]["message"]["text"])

        vk.messages.send(
            message=get_callback(from_id, message),
            random_id=utils.get_random_id(),
            peer_id=from_id,
        )
        return "ok"
    return "ok"

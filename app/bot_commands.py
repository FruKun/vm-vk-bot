from config import admin_id
from yandex_api import (
    response_get_instance,
    response_post_start_instance,
    response_post_stop_instance,
)


def get_callback(from_id: int, message: str) -> str:
    if message in ["/start", "start", "начало", "/начало"]:
        return message_start_callback(from_id)
    elif message.strip().lower() in [
        "info",
        "/info",
        "/information",
        "information",
        "/status",
        "status",
        "/информация",
        "информация",
        "/статус",
        "статус",
        "инфо",
        "/инфо",
    ]:
        return message_info_callback()
    elif message.strip().lower() in [
        "/power_on",
        "power_on",
        "on",
        "/on",
        "включить",
        "/включить",
        "запуск",
        "/запуск",
    ]:
        return message_power_on_callback()
    elif message.strip().lower() in [
        "/power_off",
        "power_off",
        "off",
        "/off",
        "выключить",
        "/выключить",
        "отключить",
        "/отключить",
    ]:
        return message_power_off_callback(from_id)
    else:
        return message_start_callback(from_id)


def message_start_callback(from_id: int) -> str:
    if from_id not in admin_id:
        return """доступные команды:
/info,
/power_on,
"""
    else:
        return """доступные команды:
/info,
/power_on,
/power_off
"""


def message_info_callback() -> str:
    if "status" in response_get_instance().json():
        return f"status: {response_get_instance().json()["status"]}"
    else:
        return "unknown error"


def message_power_on_callback() -> str:
    response = response_post_start_instance().json()
    if "error" in response:
        return response["error"]
    elif "description" in response:
        return response["description"]
    if "code" in response and response["code"] == 9:
        return "already running"
    return "unknown error"


def message_power_off_callback(from_id: int) -> str:
    if from_id not in admin_id:
        return "Permission denied"
    response = response_post_stop_instance().json()
    if "error" in response:
        return response["error"]
    elif "done" in response and response["done"]:
        return "already stopped"
    elif "response" in response:
        return response["response"]["status"]
    elif "description" in response:
        return response["description"]
    if "code" in response and response["code"] == 9:
        return "already stopping"
    return "unknown error"

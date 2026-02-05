def get_callback(message):
    if message == "/start":
        return message_start_callback()
    elif message == "/info":
        return message_info_callback()
    elif message == "/power_on":
        return message_power_on_callback()
    elif message == "/power_off":
        return message_power_off_callback()
    else:
        return "unknown command"


def message_start_callback():
    return "start callback"


def message_info_callback():
    return "info callback"


def message_power_on_callback():
    return "power on callback"


def message_power_off_callback():
    return "power off callback"

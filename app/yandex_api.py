import requests
from config import INSTANCE_ID, YANDEX_TOKEN

url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{INSTANCE_ID}"
headers = {
    "Authorization": f"Bearer {YANDEX_TOKEN}",
    "Content-Type": "application/json",
}


def response_get_instance() -> requests.Response:
    return requests.get(url, headers=headers)


def response_post_start_instance() -> requests.Response:
    return requests.post(url + ":start", headers=headers)


def response_post_stop_instance() -> requests.Response:
    return requests.post(url + ":stop", headers=headers)

from datetime import datetime, timezone

import requests
from config import INSTANCE_ID, OAUTH_YANDEX_TOKEN

iam_token = ""
expires_at = ""
url = f"https://compute.api.cloud.yandex.net/compute/v1/instances/{INSTANCE_ID}"


def get_iam_yandex_token():
    global iam_token
    global expires_at
    if (
        iam_token == ""
        or expires_at == ""
        or datetime.fromisoformat(expires_at) < datetime.now(timezone.utc)
    ):
        response = requests.post(
            "https://iam.api.cloud.yandex.net/iam/v1/tokens",
            headers={"Content-Type": "application/json"},
            json={"yandexPassportOauthToken": f"{OAUTH_YANDEX_TOKEN}"},
        )
        iam_token = response.json()["iamToken"]
        expires_at = response.json()["expiresAt"]
    return iam_token


def get_headers():
    return {
        "Authorization": f"Bearer {get_iam_yandex_token()}",
        "Content-Type": "application/json",
    }


def response_get_instance() -> requests.Response:
    return requests.get(url, headers=get_headers())


def response_post_start_instance() -> requests.Response:
    return requests.post(url + ":start", headers=get_headers())


def response_post_stop_instance() -> requests.Response:
    return requests.post(url + ":stop", headers=get_headers())

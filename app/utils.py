import requests
import json
from typing import Literal
from config import header, BETTING_POINT, ACCOUNT_POINT


def request_account_api(
    resource: str,
    method: Literal[
        "GET",
        "POST",
        "PUT",
        "DELETE",
    ],
    json_req: dict,
):
    url = ACCOUNT_POINT + resource

    response = getattr(requests, method.lower())(
        url,
        data=json.dumps(json_req),
        headers=header,
    )

    return response.json()


def request_betting_api(
    resource: str,
    method: Literal[
        "GET",
        "POST",
        "PUT",
        "DELETE",
    ],
    json_req: dict,
):
    url = BETTING_POINT + resource

    response = getattr(requests, method.lower())(
        url,
        data=json.dumps(json_req),
        headers=header,
    )

    return response.json()

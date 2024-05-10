from typing import Literal
from config import ACCOUNT_POINT, BETTING_POINT, json_req, header
import requests


def request_account_api(
    resource: str,
    method: Literal[
        "GET",
        "POST",
        "PUT",
        "DELETE",
    ],
):
    url = ACCOUNT_POINT + resource

    response = getattr(requests, method.lower())(
        url,
        data=json_req,
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
):
    url = BETTING_POINT + resource

    response = getattr(requests, method.lower())(
        url,
        data=json_req,
        headers=header,
    )

    return response.json()

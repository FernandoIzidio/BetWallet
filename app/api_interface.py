from config import json_req

from utils import request_account_api, request_betting_api  # noqa


class Account_API:
    @classmethod
    def get_account_details(cls):
        return request_account_api("getAccountDetails/", "POST", json_req)

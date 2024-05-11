from config import json_req

from utils import request_account_api, request_betting_api  # noqa


class Account_API:
    @classmethod
    def get_account_details(cls):
        return request_account_api("getAccountDetails/", "POST", json_req)

    @classmethod
    def get_account_statement(cls):
        return request_account_api("getAccountStatement/", "POST", json_req)

    @classmethod
    def get_developer_app_keys(cls):
        return request_account_api("getDeveloperAppKeys/", "POST", json_req)


class Bettings_API:
    
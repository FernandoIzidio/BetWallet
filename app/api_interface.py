from config import json_req
from utils import request_account_api, request_betting_api  # noqa
import typing


class Account_API:
    @classmethod
    def get_account_details(cls):
        return request_account_api("getAccountDetails/", "POST", json_req)

    @classmethod
    def get_account_statement(cls, json_req: dict = json_req):
        return request_account_api("getAccountStatement/", "POST", json_req)

    @classmethod
    def get_developer_app_keys(cls):
        return request_account_api("getDeveloperAppKeys/", "POST", json_req)


class Bettings_API:

    @classmethod
    def list_events_types(
        cls,
        text_query: str = "",
        event_type_ids: set[str] = "",
        market_ids: set[str] = "",
        event_ids: set[str] = "",
        competition_ids: set[str] = "",
        venue_ids: set[str] = "",
        bsp_only: bool = False,
        turn_in_play_enabled: bool = False,
        in_play_only: bool = False,
        market_betting_types: set[typing.Any] = False,
        market_countries: set[str] = "",
        market_start_time: typing.Any = "",
        withOrders: typing.Any = "",
    ):
        json_req["filter"]["textQuery"] = text_query
        json_req["filter"]["eventTypeIds"] = event_type_ids
        json_req["filter"]["marketIds"] = market_ids
        json_req["filter"]["eventIds"] = event_ids
        json_req["filter"]["competitionIds"] = competition_ids
        json_req["filter"]["venueIds"] = venue_ids
        json_req["filter"]["bspOnly"] = bsp_only
        json_req["filter"]["turnInPlayEnabled"] = turn_in_play_enabled
        json_req["filter"]["inPlayOnly"] = in_play_only
        json_req["filter"]["marketBettingTypes"] = market_betting_types
        json_req["filter"]["marketCountries"] = market_countries
        json_req["filter"]["marketStartTime"] = market_start_time
        json_req["filter"]["withOrders"] = withOrders

        return request_betting_api("listEventTypes/", "POST", json_req)

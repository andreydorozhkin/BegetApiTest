import requests
import json

account = "https://api.beget.com/api/user/"


def get_account_info():
    print(type(account))
    account_link_api = account + "getAccountInfo"
    auth_and_format = {'output_format': 'json', 'passwd': $PASSWD, 'login': $LOGIN}
    response = requests.get(account_link_api, params=auth_and_format)
    return response.json()


def print_json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print_json(get_account_info())

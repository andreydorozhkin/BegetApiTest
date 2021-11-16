import requests
import json


def print_json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


auth_and_format = {'output_format': 'json', 'passwd': 'R2dONbctqg', 'login': 'vhostbg2'}
ftp_getList = requests.get(
    "https://api.beget.com/api/ftp/getList", params=auth_and_format)
#add_ftp = {'password'}
#ftp_add = requests.post("https://api.beget.com/api/ftp/add")


print_json(ftp_getList.json())

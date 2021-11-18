import requests
import json


def print_json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


getList = {'output_format': 'json', 'passwd': 'R2dONbctqg', 'login': 'vhostbg2'}

# auth_and_format = {'input_data':'{"subdomain":"6hi.ru", "domain_id":}','output_format': 'json', 'input_format':
# 'json', 'passwd': 'R2dONbctqg', 'login': 'vhostbg2'}

response=

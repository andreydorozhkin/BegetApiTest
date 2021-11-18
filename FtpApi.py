import requests
import json


site = "https://api.beget.com/api/ftp/"
get_auth_and_format = {'output_format': 'json', 'passwd': 'R2dONbctqg', 'login': 'vhostbg2'}
post_auth_and_format = {'login': 'vhostbg2', 'passwd': 'R2dONbctqg', 'input_format': 'json', 'output_format': 'json'}


def get_list():
    command = site + "getList"
    ftp_list_response = requests.get(
        command, params=get_auth_and_format)
    parsed = ftp_list_response.json()
    return parsed['answer']['result']


def add_ftp_access(suffix, homedir, password):
    command = site + "add"
    inp_data_dict = {'suffix': suffix, "homedir": homedir, "password": password}
    params = post_auth_and_format.copy()
    params['input_data'] = json.dumps(inp_data_dict)
    ftp_status = requests.get(command, params=params)
    return ftp_status


def change_password(suffix, password):
    command = site + "changePassword"
    inp_data_dict = {'suffix': suffix, 'password': password}
    params = post_auth_and_format.copy()
    params['input_data'] = json.dumps(inp_data_dict)
    ch_pass = requests.get(command, params=params)
    return ch_pass



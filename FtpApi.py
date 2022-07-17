import requests
import json

# TODO как-то скрыть авторизацию

site = "https://api.beget.com/api/ftp/"
get_auth_and_format = {'output_format': 'json', 'passwd': $PASSWD, 'login': $LOGIN}
post_auth_and_format = {'login': $LOGIN, 'passwd': $PASSWD, 'input_format': 'json', 'output_format': 'json'}

# TODO изменить формат возврата функции get_list
# Получить список фтп доступов


def get_list():
    command = site + "getList"
    ftp_list_response = requests.get(
        command, params=get_auth_and_format)
    parsed = ftp_list_response.json()
    return parsed['answer']['result']

# Создание доступа по фтп


def add_ftp_access(suffix, homedir, password):
    command = site + "add"
    inp_data_dict = {'suffix': suffix, "homedir": homedir, "password": password}
    params = post_auth_and_format.copy()
    params['input_data'] = json.dumps(inp_data_dict)
    ftp_status = requests.get(command, params=params)
    return ftp_status

# Изменение пароля от фтп доступа


def change_password(suffix, password):
    command = site + "changePassword"
    inp_data_dict = {'suffix': suffix, 'password': password}
    params = post_auth_and_format.copy()
    params['input_data'] = json.dumps(inp_data_dict)
    ch_pass = requests.get(command, params=params)
    return ch_pass.json()

# Удаление фтп доступа


def delete_ftp_access(suffix):
    command = site + "delete"
    inp_data_dict = {'suffix': suffix}
    params = post_auth_and_format.copy()
    params['input_data'] = json.dumps(inp_data_dict)
    del_ftp = requests.get(command, params=params)
    print(del_ftp.request.url)
    return del_ftp.json()

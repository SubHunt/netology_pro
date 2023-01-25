import requests
from config import token


def _get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }


def create_folder():
    folder = 'test'
    create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = _get_headers()
    res = requests.put(f'{create_folder_url}?path={folder}', headers=headers)
    # if res.status_code == 201:
    #     print('Папка успешно создана')
    # elif res.status_code == 409:
    #     print('Такая папка уже существует')
    # else:
    #     print('Ошибка на сервере')
    return res.status_code


if __name__ == '__main__':
    cr_fold = create_folder()

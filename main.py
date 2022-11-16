

import os
import requests

# task 2
TOKEN = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]
def requests_get(url_all):
    resp = (requests.get(url) for url in url_all)
    return resp


def smartest():
    superhero = []
    for item in requests_get(urls):
        intelligence = item.json()
        for power_stats in intelligence['results']:
            superhero.append({'name': power_stats['name'], 'intelligence':
                 power_stats['powerstats']['intelligence'],})
    intelligence_superhero = 0
    name = ''
    for intelligence_hero in superhero:
        if intelligence_superhero < int(intelligence_hero['intelligence']):
            intelligence_superhero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный герой - {name}, его интелект: {intelligence_superhero}")


smartest()


# task 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            print('Файл, успешно загружен!')
        else:
            print(f"Ошибка загрузки! Код ошибки: {responce.status_code}")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:/Users/DNS/OneDrive/Desktop/new.txt"
    token = os.getenv('TOKEN_YaD_VOLNOFF')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)

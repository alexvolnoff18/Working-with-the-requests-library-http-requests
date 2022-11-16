import requests

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

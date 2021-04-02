from pip._vendor import requests

# Задание №1


class Superhero:
    def __init__(self, name, id):
        self.name = name
        self.id = id


hulk = Superhero('Hulk', '332')
captain = Superhero('Captain_America', '149')
thanos = Superhero('Thanos', '655')
superheroes_list = []
links_list = []
heroes_list = []
id_list = []
intel_dict = {}


def add_superheroes():
    new_list = [hulk, captain, thanos]
    superheroes_list.extend(new_list)
    return superheroes_list


def add_links():
    link = 'https://superheroapi.com/api/2619421814940190/search/'
    hulk_link = link + hulk.name
    captain_link = link + captain.name
    thanos_link = link + thanos.name
    new_links = [hulk_link, captain_link, thanos_link]
    links_list.extend(new_links)
    return links_list


def add_ids():
    web = 'https://superheroapi.com/api/2619421814940190/'
    web_hulk = web + hulk.id + '/powerstats'
    web_captain = web + captain.id + '/powerstats'
    web_thanos = web + thanos.id + '/powerstats'
    new_web = [web_hulk, web_captain, web_thanos]
    id_list.extend(new_web)
    return id_list


def find_intelligence():
    while True:
        for line in id_list:
            response = requests.get(line)
            final = response.json()
            heroes_list.append(final)
            for content in heroes_list:
                for key, value in content.items():
                    if key == 'intelligence':
                        intel_dict[content['name']] = int(value)
                        Keymax = max(intel_dict, key=intel_dict.get)
        return f'Самый умный супергерой: {Keymax}'


# print(add_superheroes())
# print(add_links())
# print(heroes_list)
print(add_ids())
print(find_intelligence())
print(intel_dict)


# Задание №2


class YaUploader:
    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, params=params)
        return response.json()

    def upload(self, file_path):
        href = self._get_upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        return 'Загрузка прошла успешно'


if __name__ == '__main__':
    uploader = YaUploader(token='_')
    # result = uploader.upload(r'C:\Project\test.txt')


# Задание №3


class Stackoverflow:

    def get_python_tags(self):
        url = "https://api.stackexchange.com/2.2/questions"
        params = {'todate': '1617321600', 'fromdate': '1617148800', 'sort': 'activity', 'tagged': 'Python',
                  'site': 'stackoverflow'}
        response = requests.get(url, params=params, timeout=5)
        return print(response.json())

    get_python_tags(self=None)

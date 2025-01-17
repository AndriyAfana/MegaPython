import requests
import random

random_page = random.randint(1, 7438)
page_size = 1

url = f'https://api.disneyapi.dev/character?pageSize={page_size}&page={random_page}'

response = requests.get(url)

if response.ok:
        json_data = response.json()
        name = json_data['data']['name']
        films = json_data['data']['films']
        shortFilms = json_data['data']['shortFilms']
        tvShows = json_data['data']['tvShows']
        videoGames = json_data['data']['videoGames']
        print(f"Character: {name}")
        print(f"Films: {''.join(films)}")
        print(f"Short Films: {''.join(shortFilms)}")
        print(f"TV Shows: {''.join(tvShows)}")
        print(f"Video Games: {''.join(videoGames)}")
else:
        print('Щось пішло не так...')
        print(f'{response.status_code=}')
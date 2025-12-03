import requests
repo_owner = 'octocat'
repo_name = 'Hello-World'
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    print(f"Репозиторий: {data['name']}")
    print(f"Описание: {data['description']}")
    print(f"Звёзды: {data['stargazers_count']}")
else:
    print('Ошибка получения информации о репозитории')
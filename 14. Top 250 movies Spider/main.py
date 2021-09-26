import requests
from bs4 import BeautifulSoup
from requests.api import head

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
}
base_url = "https://movie.douban.com/top250"
top_250 = []

def is_Chinese(str):
    if str.split()[0] == '/':
        return False
    return True   

for offset in range(0, 250, 25):
    params = {
    "start": offset,
    "filter": "",
    }
    
    res = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    movies = soup.find_all(name="span", class_="title")
    for movie in movies:
        moive_title = movie.get_text()
        if is_Chinese(moive_title):
            top_250.append(movie.get_text())

with open ("14. Top 250 movies Spider/top_250.txt", 'w', encoding="utf-8") as f:
    index = 1
    for movie in top_250:
        f.write(f"{index}.{movie}\n")
        index += 1
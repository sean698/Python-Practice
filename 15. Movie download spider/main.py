import requests
from bs4 import BeautifulSoup

baseURL = "https://www.ygdy8.com/html/gndy/dyzz/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
movie_titles = []
movie_urls = []

def get_page(url):
    res = requests.get(url, headers=headers)
    res.encoding = "gb2312"
    return res

def get_title_url(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all("a", class_="ulink")
    for link in links:
        title = link.text
        url = link['href']
        movie_titles.append(title)
        # For some unknown reasons, the urls should be corrected
        date = url.split('/')[4]
        movie_num = int(url.split('/')[5].split('.')[0]) - 5
        url = f"https://www.dytt8.net/html/gndy/dyzz/{date}/{movie_num}.html"
        movie_urls.append(url)

def get_magnet_url(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    link = soup.find("a", target="_blank")
    magnet = link['href']
    return magnet

def get_user_choice():
    return (input("Which movie would you like to download? Enter the index: "))

def print_title():
    index = 1
    for movie in movie_titles:
        print('\n')
        print(f"{index}. {movie}")
        index += 1

if __name__ == "__main__":
    page = get_page(baseURL)
    get_title_url(page)
    print_title()
    choice = int(get_user_choice())
    url = movie_urls[choice - 1]
    page = get_page(url)
    magnet = get_magnet_url(page)
    print('\n')
    print(magnet)




import requests
from bs4 import BeautifulSoup
import os
import ctypes

def get_image():
    #if you want different search options, go to https://wallhaven.cc/random
    #choose wanted options, hit reload and paste the link here
    url = "https://wallhaven.cc/search?categories=010&purity=010&resolutions=1920x1080&sorting=random&order=desc"

    pic_page = soup_from_url(url).find("a", {"class" : "preview"}).get("href")
    img_url = soup_from_url(pic_page).find("img", {"id" : "wallpaper"}).get("src")

    img_data = requests.get(img_url).content
    with open("wallpaper.jpg", 'wb') as handler:
        handler.write(img_data)

    print("Link to the image page : " + pic_page)

    set_image()

def set_image():
    path = os.getcwd() + "/wallpaper.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

def soup_from_url(url):
    html = requests.get(url).content
    return BeautifulSoup(html, features="html.parser")

if __name__ == "__main__":
    get_image()

from os import name
import requests
import fake_useragent
from bs4 import BeautifulSoup
import time
import json


def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/resume?isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&search_period=0&order_by=relevance&filter_exp_period=all_time&relocation=living_or_relocation&text={text}&gender=unknown&page=1",
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_count = int(
            soup.find("div", attrs={"class": "pager"}).find_all("span", recursive=False)[-1].find("a").find(
                "span").text())
    except:
        return
    for page in range(page_count):
        data = requests.get(
            url=f"https://hh.ru/search/resume?isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&search_period=0&order_by=relevance&filter_exp_period=all_time&relocation=living_or_relocation&text={text}&gender=unknown&page={page}",
            headers={"user-agent": ua.random}
        )
        if data.status_code !=200:
            continue
        soup = BeautifulSoup(data.content, "lxml")
        soup.find_all()




def get_resume(link):
    pass


if __name__ == '__main__':
    get_links('python')

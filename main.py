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
    print(data.content)


def get_resume(link):
    pass


if __name__ == '__main__':
    get_links('python')

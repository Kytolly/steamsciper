import requests
from . import preparser
from bs4 import BeautifulSoup
from lxml import etree
import json
import csv

from src.utils.logger import getMyLogger
logger = getMyLogger()

def get_game_items(response):
    # soup = BeautifulSoup(response, "html.parser")
    # game_items = soup.find_all("a", class_="search_result_row")
    html = etree.HTML(response.text, etree.HTMLParser(encoding="UTF-8"))
    game_items = html.xpath('/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a')
    raw_games = []

    for item in game_items:
        game = {}

        # 补充爬game的逻辑
        
        logger.debug("src/scraper/spider.py: now game spidering is:", game)
        raw_games.append(game)
    return raw_games 

# 将字典列表写入JSON文件
def save_raw_games_json(raw_games):
    with open('data/raw/games_data.json', 'w', encoding='utf-8') as f:
        json.dump(raw_games, f, ensure_ascii=False, indent=4)
    return raw_games

# 将字典列表写入csv文件
def save_raw_games_csv(raw_games):
    with open('data/raw/raw_games.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = raw_games[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for game in raw_games:
            writer.writerow(game)
    return raw_games

# 爬虫程序，获取响应，保存数据
def spiderRunning(url):
    response = preparser.get_response(url)
    raw_games = get_game_items(response)
    save_raw_games_json(raw_games)
    save_raw_games_csv(raw_games)
    return raw_games
import requests
from lxml import etree
import csv
from decimal import Decimal
import datetime

url = 'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&ndl=1'
headers = {
    'User-Agent': 'Mozilla/5.0 ''Accept-Language:zh-CN' ' (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers, verify=False)
html = etree.HTML(resp.text, etree.HTMLParser(encoding="UTF-8"))
divs = html.xpath('/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a')
for div in divs:
    names = div.xpath('//*[@id="search_resultsRows"]/a/div[2]/div[1]/span/text()')
    prices = div.xpath('//*[@id="search_resultsRows"]/a/div[2]/div[4]/div/div/div/div/text()')
    dates = div.xpath('//*[@id="search_resultsRows"]/a/div[2]/div[2]/text()')
    try:
        evaluates = div.xpath('//*[@id="search_resultsRows"]/a/div[2]/div[3]/span[@class="search_review_summary mixed"]/@data-tooltip-html')
    except:
        evaluates="暂无评测"
for name, price, date, evalute in zip(names, prices, dates, evaluates):
    data = f"Name: {name.strip()} , Price: {price.strip()} , Date: {date.strip()},Evaluate:{str(evalute).replace('<br>','').strip()}"
    print(data)
resp.close()



raw_game = {
    "Gid": 0,
    "name": "default",
    "download_num": 0,
    "comments": 0,
    "pos_comments": 0,
    "url": "default",
    "thumbnail": "default",
    "create_date": datetime(2024, 7, 14),
    "publish_date": datetime(2024, 7, 14),
    "tag": "default",
    "price": Decimal.from_float(0.0),
    "publisher": "default",
    "online_players": 0,
    "platform": "windows",
}
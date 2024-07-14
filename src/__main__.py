import os
import sys
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

import src.scraper.spider as sp
import src.processing.cleaner as cl

url_hot = 'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&ndl=10'

if __name__ == '__main__':
    raw_games = sp.spiderRunning(url_hot)
    cleaned_games = cl.data_clean(raw_games)
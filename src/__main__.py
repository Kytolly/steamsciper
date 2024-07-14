import os
import sys
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

from src.scraper.spider import spiderRunning

url = 'https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers&ndl=1'
if __name__ == '__main__':
    spiderRunning(url)
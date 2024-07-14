from datetime import datetime
from decimal import *
from . import utils

from src.utils.logger import getMyLogger
logger = getMyLogger()

# 爬取的数据是list, 转化成dict进行去重,如果两个游戏gid不一样就是不同游戏
# 尽管比如说gameB是gameA的后日谈，它们是一样的名字，也认为这是两个游戏
def data_distinct(raw_games):
    distincted_games = {}
    for game in raw_games:
        try: 
            gid = int(game["Gid"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game Gid: cannot be controved to int", game["Gid"])
            continue

        game_details = {}

        try: 
            name = str(game["Name"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game name: cannot be controved to string", game["name"])
            name = "default"
        game_details["name"] = name

        try: 
            download_num = int(game["download_num"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game download_num: cannot be controved to int", game["download_num"])
            download_num = 0
        game_details["download_num"] = download_num

        try: 
            comments = int(game["comments"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game comments: cannot be controved to int", game["comments"])
            comments = 0
        game_details["comments"] = comments

        try: 
            pos_comments = int(game["pos_comments"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game pos_comments: cannot be controved to int", game["pos_comments"])
            pos_comments = 0
        game_details["pos_comments"] = pos_comments

        try: 
            url = str(game["url"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game url: cannot be controved to string", game["url"])
            url = "default"
        game_details["url"] = url

        try: 
            thumbnail = str(game["thumbnail"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game thumbnail: cannot be controved to string", game["thumbnail"])
            thumbnail = 0
        game_details["thumbnail"] = thumbnail

        try: 
            create_date = utils.strParseIntoDatetime(game["create_date"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game create_date: cannot be controved to datetime object", game["create_date"])
            create_date = datetime(2024, 7, 14)
        game_details["create_date"] = create_date\
        
        try: 
            publish_date = utils.strParseIntoDatetime(game["publish_date"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game publish_date: cannot be controved to datetime object", game["publish_date"])
            publish_date = datetime(2024, 7, 14)
        game_details["publish_date"] = publish_date

        try: 
            tag = str(game["tag"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game tag: cannot be controved to string", game["tag"])
            tag = "default"
        game_details["tag"] = tag

        try: 
            price = utils.strParseIntoDecimal(game["price"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game price: cannot be controved to decimal object", game["price"])
            price = Decimal(0)
        game_details["price"] = price

        try: 
            publisher = str(game["publisher"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game publisher: cannot be controved to string", game["publisher"])
            publisher = Decimal(0)
        game_details["publisher"] = publisher

        try: 
            online_players = int(game["online_players"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game online_players: cannot be controved to int", game["online_players"])
            online_players = 0
        game_details["online_players"] = online_players

        try: 
            platform = str(game["platform"])
        except ValueError:
            logger.error("src/processing/cleaner.py: Invalid game platform: cannot be controved to string", game["platform"])
            platform = "default"
        game_details["platform"] = platform

        distincted_games[gid] = game_details
    return distincted_games

# 作异常值检测，可能要用到统计的方法
# 现在没有数据，暂时不做处理
def data_detect(distincted_games):
    return distincted_games

def data_clean(raw_games):
    distincted_games = data_distinct(raw_games)
    games = data_detect(distincted_games)
    return games
import requests
import logging
from . import preparser

def spiderRunning(url):
    preparser.get_text(url)
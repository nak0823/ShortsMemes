import random

from Utils import config
from Utils import logger
from Mods import reddit as reddit
from Mods import compiler as compiler
from Auto import youtube as youtube
from Mods import title as Title

shorts_amount = config.shorts_amount

def run():
    reddit.auto_reddit()
    compiler.compile(True)
    youtube.auto_upload()

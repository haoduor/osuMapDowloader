from model import maps
import json


class mapSpider:
    def __init__(self):
        pass

    @staticmethod
    def getTestData():
        with open('temp.json') as f:
            res = json.load(f)
        return res

import requests
import json


class maps(object):
    def __init__(self):
        self.defaultMapUrl = 'https://osu.ppy.sh/beatmapsets/search?m=0'
        # self.userSession = userSession

    def get(self, pages=1):
        mapsID = []
        DUrl = self.defaultMapUrl + '&page=' + str(pages)

        r = requests.get(DUrl)
        res = r.json()

        for i in range(len(res)):
            mapsID.append(res[i]['id'])

        return mapsID

import log

logger = log.getlogger()


class beatmaps():
    beatmap_id = 0
    mode_int = 0
    mode = ''
    ranked = 0

    def __init__(self, beatmap_id=0, mode_int=0, mode='', ranked=0):
        self._parent = None
        self.beatmap_id = beatmap_id
        self.mode_int = mode_int
        self.mode = mode
        self.ranked = ranked

    def setParent(self, maps):
        self._parent = maps

    def getParent(self):
        return self._parent

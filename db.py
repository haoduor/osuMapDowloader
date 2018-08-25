import shelve


class data(object):
    def __init__(self, filename):
        self.infor = shelve.open(filename)

    def get(self, key):
        res = None
        try:
            res = self.infor[key]
        except KeyError:
            return None
        return res

    def insert(self, key, value):
        self.infor[key] = value

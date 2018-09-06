import yaml


class baseMapper:
    def __init__(self):
        self.relation = None

    def loadConf(self):
        path = 'mapper/mapper/%s.yaml' % self.__class__.__name__
        with open(path) as f:
            self.relation = yaml.load(f)
        return self.relation

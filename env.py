import yaml


def value(v):
    f = None
    f = open('config.yaml')
    res = yaml.load(f)
    return res[v]

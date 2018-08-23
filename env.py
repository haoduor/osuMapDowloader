import yaml


def value(value):
    f = None
    f = open('config.yaml')
    res = yaml.load(f)
    return res[value]

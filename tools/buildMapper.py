from model import maps

if __name__ == '__main__':
    f = open('../mapper/mapper/mapsMapper.yaml', 'w')

    m = maps()
    t = m.__dict__.keys()

    for i in t:
        f.writelines(i+':\n')

    print t
class maps():
    map_id = 0
    submitted_time = ''
    last_updated = ''
    ranked_date = ''
    source = ''

    def __init__(self, map_id=0, submitted_time='', last_updated='', ranked_date='', source=''):
        self.map_id = map_id
        self.submitted_time = submitted_time
        self.last_updated = last_updated
        self.ranked_date = ranked_date
        self.source = source

    def __getitem__(self, item):
        return self.__dict__[item]

class DataDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von Feld-Daten
    """

    def __init__(self):
        super().__init__(self)

    def append(self, name, data):
        if name not in self.keys():
            self[name] = data


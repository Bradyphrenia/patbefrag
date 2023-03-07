class DataDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von Feld-Daten
    """

    def __init__(self):
        super().__init__(self)

    def append(self, key, value):
        self.setdefault(key, value)

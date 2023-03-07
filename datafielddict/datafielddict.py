class DataFieldDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von Feld-Parametern
    """

    def __init__(self):
        super().__init__(self)

    def append(self, key, value):
        self.setdefault(key, value)

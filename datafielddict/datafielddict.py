class DataFieldDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von Feld-Parametern
    """

    def __init__(self):
        super().__init__(self)

    def append(self, position, field_list):
        if position not in self.keys():
            self[position] = field_list

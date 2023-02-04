class CheckBoxDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von CheckBoxen
    """

    def __init__(self, dict_):
        super().__init__(self)
        self.update(dict_)

    def append(self, position, ckb):
        if position not in self.keys():
            self[position] = ckb

    def check(self, position):
        if 0 <= position < len(self):
            self[position].setChecked(True)
            [self[c].setChecked(False) for c, _ in enumerate(self) if c != position]

    def bind(self, position):
        if 0 <= position < len(self):
            return self[position].clicked.connect(lambda: self.check(position))

    def bindall(self):
        for c, _ in enumerate(self):
            self.bind(c)

    def note(self):
        for c, _ in enumerate(self):
            if self[c].isChecked():
                return ['1', '2', '3', '4', '5'][c]
        return '9'

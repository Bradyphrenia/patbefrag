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
            for c in self:
                if c != position:
                    self[c].setChecked(False)

    def bind(self, position):
        if 0 <= position < len(self):
            return self[position].clicked.connect(lambda: self.check(position))

    def bindall(self):
        for c, _ in enumerate(self):
            self.bind(c)

    @property
    def note(self):
        for entry in self.keys():
            if self[entry].isChecked():
                return ['1', '2', '3', '4', '5'][entry]
        return '9'  # no checkbox is checked

    @property
    def position(self):
        for entry in self.keys():
            if self[entry].isChecked():
                return [0, 1, 2][entry]
        return 3  # no checkbox is checked

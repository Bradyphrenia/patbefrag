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

    def check(self, key):
        for entry in self.keys():
            entry.setChecked(False) if key == entry else entry.setChecked(True)

    def bind(self, position):
        if 0 <= position < len(self):
            return self[position].clicked.connect(lambda: self.check(position))

    def bindall(self):
        for c, _ in enumerate(self):
            self.bind(c)

    def note(self):
        for entry in self.keys():
            if entry.isChecked():
                # nothing will be returned if !entry.isChecked()
                return ['1', '2', '3', '4', '5'][entry]
        return '9'

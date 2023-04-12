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

    def check(self, value):
        for val in self.values():
            val.setChecked(True) if val == value else val.setChecked(False)

    def bind(self, value):
        if value in self.values():
            return value.clicked.connect(lambda: self.check(value))

    def bindall(self):
        for val in self.values():
            self.bind(val)

    @property
    def note(self):
        for entry in self.keys():
            if self[entry].isChecked():
                return ['1', '2', '3', '4', '5'][entry]
        return '9'  # no checkbox is checked

    @property
    def position(self):
        for entry in self.keys():
            print(entry)
            if self[entry].isChecked():
                return [0, 1, 2, 3][entry]
        return 3  # no checkbox is checked

class CheckBoxDict(dict):
    """
    von Dictionary abgeleitete Klasse zur Speicherung von CheckBoxen
    """

    def __init__(self, dict_):
        super().__init__(self)
        self.update(dict_)

    def append(self, key, value):
        self.setdefault(key, value)

    def check(self, value):
        for val in self.values():
            val.setChecked(True) if val == value else val.setChecked(False)

    def bind(self, value):
        if value in self.values():
            return value.clicked.connect(lambda: self.check(value))

    def bindall(self):
        for val in self.values():
            self.bind(val)

    def note(self):
        for entry in self.keys():
            if self[entry].isChecked():
                # nothing will be returned if !entry.isChecked()
                return ['1', '2', '3', '4', '5'][entry]
        return '9'

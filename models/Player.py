class Player():
    def __init__(self, name, work_group=""):
        self.name = name
        self.work_group = work_group
        self._key = name.replace(" ","")
class BusStop:
    def __init__(self, code: str, roadname: str, desc: str, lat: float, long: float):
        self.code = code
        self.roadname = roadname
        self.desc = desc
        self.lat = lat
        self.long = long


class Directory:
    def __init__(self):
        self._map = {}

    def addStop(self, stop: BusStop):
        self._map[stop.code] = stop

    def removeStop(self, stop: BusStop):
        del self._map[stop.code]

    def __getitem__(self, key: str):
        return self._map[key]

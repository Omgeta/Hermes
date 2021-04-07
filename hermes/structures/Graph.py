from .BusStop import BusStop


class Graph:
    '''
    Adjacency List/Map to store nodes connected by directed, weighted edges.
    [
        OriginCode: [(DestinationCode, Distance, BusServicesList), ...]
        1: [(2, 0.5, ["10", "101A"])]
        2: ...
    ]
    '''

    def __init__(self):
        self._adjmap = {}

    def addNode(self, node: BusStop):
        self._adjmap[node.code] = []

    def removeNode(self, node: BusStop):
        del self._adjmap[node.code]

    def addRoute(self, start: BusStop, end: BusStop, dist: int, service: str):
        if not self._adjmap[start.code]:
            self._adjmap[start.code] = (end.code, dist, [service])
        else:
            self._adjmap[start.code][2].append(service)

    def removeRoute(self, start, end):
        for route in self._adjmap[start.code]:
            if route[0].code == end:
                del route

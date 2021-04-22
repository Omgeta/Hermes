class Route:
    def __init__(self, distance: float, *services: str):
        self._distance = distance
        self._services = [service for service in services]

    def addService(self, service: str):
        if service not in self._services:
            self._services.append(service)
        else:
            print(f"Attempted to add existing service {service}")

    def removeService(self, service: str):
        if service in self._services:
            self._services.remove(service)
        else:
            print(f"Attempted to remove existing service {service}")

    def getDistance(self):
        return self._distance

    def getServices(self):
        return self._services


class Graph:
    '''
    Adjacency List/Map to store nodes connected by directed, weighted edges.

    {
        start: {
            end: Route(dist, [services])
        },
        ...
    }
    '''

    def __init__(self):
        self._map = {}

    def __getitem__(self, key: str) -> dict:
        return self._map[key]

    def __setitem__(self, key: str, value: dict):
        self._map[key] = value

    def addNode(self, node: str):
        if node not in self._map:
            self[node] = {}
        else:
            print(f"Attempted to add already existing node {node}.")

    def removeNode(self, node: str):
        if node in self._map:
            del self[node]
        else:
            print(f"Attempted to remvove non-existing node {node}")

    def addRoute(self, startNode: str, endNode: str, dist: float, service: str):
        if endNode in self[startNode] and dist >= self[startNode][endNode].distance:
            self[startNode][endNode].addService(service)
        else:
            self[startNode][endNode] = Route(dist, service)

    def removeRoute(self, startNode: str, endNode: str):
        del self[startNode][endNode]

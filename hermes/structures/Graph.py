class Graph:
    """
    Basic 2D adjacency map
    """

    def __init__(self):
        self._map = {}

    def __getitem__(self, key):
        return self._map[key]

    def __setitem__(self, key, value):
        self._map[key] = value

    def __contains__(self, key):
        return key in self._map

    def addNode(self, node: str):
        """
        Adds an unconnected node to the graph.

            Parameters:
                node (str): Name of the new node
        """
        if node not in self:
            self[node] = {}

    def removeNode(self, node: str):
        """
        Removed an existing unconnected node from the graph.

            Parameters:
                node (str): Name of node to remove
        """
        if node in self:
            del self[node]

    def addEdge(self, a: str, b: str, weight: float, data):
        """
        Add a weighted edge between two nodes with some data.

            Parameters:
                a (str): Name of starting node
                b (str): Name of ending node
                weight (float): Weight between starting and ending nodes
                data (any): Some data to carry
        """
        self[a][b] = (weight, data)

    def editEdge(self, a: str, b: str, new):
        """
        Edits the data of an existing edge between two nodes.

            Parameters:
                a (str): Name of starting node
                b (str): Name of ending node
                new (any): Some new data to replace old data
        """
        if a in self and b in self[a]:
            weight, data = self[a][b]
            self[a][b] = (weight, new)

    def removeEdge(self, a: str, b: str):
        """
        Removes an edge between two nodes

            Parameters:
                a (str): Name of starting node
                b (str): Name of ending node
        """
        del self[a][b]


class BusGraph(Graph):
    """
    Advanced 2D adjacency map of bus stops connected by the shortest bus routes, each with a list of connected services.
    """

    def addStop(self, stop: str):
        """
        Adds a bus stop to the graph

            Parameters:
                stop (str): Bus stop code to add
        """
        super().addNode(stop)

    def removeStop(self, stop: str):
        """
        Removes a bus stop from the graph

            Parameters:
                stop (str): Bus stop code to remove
        """
        super().removeNode(stop)

    def addRoute(self, a: str, b: str, dist: float, service: str):
        """
        Adds shortest bus route between two stops on the graph and the services that pass through it.

            Parameters:
                a (str): Code of starting stop
                b (str): Code of ending stop
                dist (float): Distance between starting and ending stops
                service (str): Service passing through the route
        """
        if a in self:
            if b in self[a]:
                curr_dist, services = self[a][b]
                if dist < curr_dist:  # if shortest path exists, overwrite old path
                    self.removeRoute(a, b)
                    self.addRoute(a, b, dist, service)
                elif dist == curr_dist:  # if same distance, add new service to path
                    if service not in services:
                        services.append(service)
                    super().editEdge(a, b, services)
            else:  # if no path exists, add new path
                super().addEdge(a, b, dist, [service])

    def removeRoute(self, a: str, b: str):
        """
        Removes a bus route between two stops on the graph.

            Parameters:
                a (str): Code of starting stop
                b (str): Code of ending stop
        """
        super().removeEdge(a, b)

    def getDistance(self, a: str, b: str) -> float:
        """
        Returns distance between two stops on the graph.

            Parameters:
                a (str): Code of starting stop
                b (str): Code of ending stop

            Returns:
                dist (float): Distance between starting and ending stops.
        """
        if a in self and b in self[a]:
            dist, services = self[a][b]
            return dist

    def getServices(self, a: str, b: str) -> list:
        """
        Returns a list of services between two stops on the graph.

            Parameters:
                a (str): Code of starting stop
                b (str): Code of ending stop

            Returns:
                services (list): List of services passing through starting and ending stops.    
        """
        if a in self and b in self[a]:
            dist, services = self[a][b]
            return services

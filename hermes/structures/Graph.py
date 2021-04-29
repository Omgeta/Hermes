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

    def __inclusion__(self, key):
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

    def addEdge(self, from: str, to: str, weight: float, data):
        """
        Add a weighted edge between two nodes with some data.

            Parameters:
                from (str): Name of starting node
                to (str): Name of ending node
                weight (float): Weight between starting and ending nodes
                data (any): Some data to carry
        """
        self[from][to] = (weight, data)

    def editEdge(self, from: str, to: str, new):
        """
        Edits the data of an existing edge between two nodes.

            Parameters:
                from (str): Name of starting node
                to (str): Name of ending node
                new (any): Some new data to replace old data
        """
        if from in self and to in self[from]:
            weight, data = self[from][to]
            self[from][to] = (weight, new)

    def removeEdge(self, from: str, to: str):
        """
        Removes an edge between two nodes

            Parameters:
                from (str): Name of starting node
                to (str): Name of ending node
        """
        del self[from][to]


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

    def addRoute(self, from: str, to: str, dist: float, service: str):
        """
        Adds shortest bus route between two stops on the graph and the services that pass through it.

            Parameters:
                from (str): Code of starting stop
                to (str): Code of ending stop
                dist (float): Distance between starting and ending stops
                service (str): Service passing through the route
        """
        if from in self:
            if to in self[from]:
                curr_dist, services = self[from][to]
                if dist < curr_dist:  # if shortest path exists, overwrite old path
                    self.removeRoute(from, to)
                    self.addRoute(from, to, dist, service)
                elif dist == curr_dist:  # if same distance, add new service to path
                    if service not in services:
                        services.append(service)
                    super().editEdge(from, to, services)
            else:  # if no path exists, add new path
                super().addEdge(from, to, dist, [service])

    def removeRoute(self, from: str, to: str):
        """
        Removes a bus route between two stops on the graph.

            Parameters:
                from (str): Code of starting stop
                to (str): Code of ending stop
        """
        super().removeEdge(from, to)

    def getDistance(self, from: str, to: str) -> float:
        """
        Returns distance between two stops on the graph.

            Parameters:
                from (str): Code of starting stop
                to (str): Code of ending stop

            Returns:
                dist (float): Distance between starting and ending stops.
        """
        if from in self and to in self[from]:
            dist, services = self[from][to]
            return dist

    def getServices(self, from: str, to: str) -> list:
        """
        Returns a list of services between two stops on the graph.

            Parameters:
                from (str): Code of starting stop
                to (str): Code of ending stop

            Returns:
                services (list): List of services passing through starting and ending stops.    
        """
        if from in self and to in self[from]:
            dist, services = self[from][to]
            return services

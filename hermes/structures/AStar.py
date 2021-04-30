from hermes.structures.Graph import BusGraph
from hermes.structures.PriorityQueue import PriorityQueue, Node
from hermes.db import get_db
from collections import defaultdict


class AStar:
    """
    A* Search Algorithm
    """

    def __init__(self, adjmap: BusGraph):
        self.adjmap = adjmap

        self.srccode = None
        self.dstcode = None
        self.stops = {}

    def addStop(self, code: str):
        """
        Memoize bus stop details

            Parameters:
                code (str): Bus stop code to find and memoize
        """
        conn = get_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM BusStops WHERE BusStopCode = ?", (code, ))
        stop = cur.fetchone()

        self.stops[code] = stop

    def reconstruct_path(self, came_from: list, current_code: str) -> tuple:
        """
        Return final path between start and end stop.

            Parameters:
                came_from (list): List tracking which stops were passed through to the current stop.
                current_code (str): Code of end stop.

            Returns:
                total_path (list): List of stops that were passed through from start to end.
                total_route (list): List of routes between each pair of stops from start to end.
        """

        def getbustuple(code): return tuple(self.stops[code])[:3]

        total_path = [getbustuple(current_code)]
        while current_code in came_from:
            current_code = came_from[current_code]
            total_path.insert(0, getbustuple(current_code))

        total_route = []
        for i in range(len(total_path) - 1):
            curr_code, next_code = total_path[i][0], total_path[i+1][0]
            route = self.adjmap[curr_code][next_code]
            total_route.append(route)
        total_route.append((0.0, []))

        # print(total_path, len(total_path))
        return total_path, total_route

    def search(self, srccode: str, dstcode: str) -> list:
        """
        Search shortest path from start to end stop using A* Algorithm.

            Parameters:
                srccode (str): Starting bus stop code.
                dstcode (String): Ending bus stop code.

            Returns:
                total_path (list): List of stops that were passed through from start to end.
        """
        self.srccode, self.dstcode = srccode, dstcode
        self.addStop(self.srccode)
        self.addStop(self.dstcode)

        pq = PriorityQueue()
        start_node = Node(0, srccode)
        pq.insert(start_node)

        came_from = {}

        g = defaultdict(lambda: float("inf"))
        g[srccode] = 0

        f = defaultdict(lambda: float("inf"))
        f[srccode] = 0

        while len(pq) > 0:
            curr_node = pq.removeminimum()
            curr_code = curr_node.value
            if curr_code == dstcode:
                return self.reconstruct_path(came_from, curr_code)

            for neighbour_code in self.adjmap[curr_code]:
                if neighbour_code not in self.stops:
                    self.addStop(neighbour_code)

                temp_g = g[curr_code] + self.d(curr_code, neighbour_code)
                if temp_g < g[neighbour_code]:
                    came_from[neighbour_code] = curr_code
                    g[neighbour_code] = temp_g
                    f[neighbour_code] = g[neighbour_code] + \
                        self.h(neighbour_code)
                    if neighbour_code not in pq.pq and neighbour_code not in pq.removed:
                        pq.insert(Node(f[neighbour_code], neighbour_code))

        return []

    def d(self, a: str, b: str) -> float:
        """
        g-cost fn
        Distance between two bus stops on a route.

            Parameters:
                a (str): First bus stop code.
                b (str): Second bus stop code.

            Returns:
                dist (float): Distance from a to b.
        """
        dist = self.adjmap.getDistance(a, b)
        return dist

    def h(self, a: str) -> float:
        """
        h-cost fn (heuristic cost function)
        Linear euclidean distance between a bus stop and the ending stop.

            Parameters:
                a (str): Bus stop code.

            Returns:
                dist (float): Linear euclidean distance between a and ending stop.
        """
        stop = self.stops[a]
        end_stop = self.stops[self.dstcode]

        return abs(end_stop["Latitude"] - stop["Latitude"]) + abs(end_stop["Longitude"] - stop["Longitude"])

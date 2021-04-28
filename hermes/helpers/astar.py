from hermes.structures.Graph import Graph, Route
from hermes.structures.PriorityQueue import PriorityQueue, Node
from hermes.db import get_db
from collections import defaultdict
import math


class AStar:
    def __init__(self, adjmap: Graph):
        self.adjmap = adjmap
        self.conn = get_db()

        self.srccode = None
        self.dstcode = None
        self.stops = {}

    def addStop(self, code: str):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM BusStops WHERE BusStopCode = {code}")
        stop = cur.fetchone()

        self.stops[code] = stop

    def reconstruct_path(self, came_from: list, current_code: str):
        total_path = [current_code]
        while current_code in came_from:
            current_code = came_from[current_code]
            total_path.insert(0, current_code)
        return total_path

    def search(self, srccode: str, dstcode: str) -> list:
        self.srccode, self.dstcode = srccode, dstcode
        self.addStop(self.srccode)
        self.addStop(self.dstcode)

        pq = PriorityQueue()
        start_node = Node(0, srccode)
        end_node = Node(0, dstcode)
        pq.insert(start_node)

        came_from = {}

        g = defaultdict(lambda: float("inf"))
        g[srccode] = 0

        f = defaultdict(lambda: float("inf"))
        f[srccode] = 0

        while len(pq) > 0:
            curr_node = pq.minimum()
            curr_code = curr_node.value
            if curr_node == end_node:
                return self.reconstruct_path(came_from, curr_code)

            pq.remove(curr_node)
            for neighbour_code in self.adjmap[curr_code]:
                temp_g = g[curr_code] + self.d(curr_code, neighbour_code)
                if temp_g < g[neighbour_code]:
                    came_from[neighbour_code] = curr_code
                    g[neighbour_code] = temp_g
                    f[neighbour_code] = g[neighbour_code] + \
                        self.h(neighbour_code)
                    if neighbour_code not in pq.pq:
                        pq.insert(Node(f[neighbour_code], neighbour_code))

        return -1

    def d(self, curr_code, next_code: str) -> int:
        route = self.adjmap[curr_code][next_code]
        return route.getDistance()

    def h(self, next_code: str) -> float:
        curr_stop = self.stops[next_code]
        end_stop = self.stops[self.dstcode]

        return abs((end_stop["Latitude"] - curr_stop["Latitude"])) + abs((end_stop["Longitude"] - curr_stop["Longitude"]))

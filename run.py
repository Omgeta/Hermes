import pickle
import pprint
from hermes.structures.BusStop import BusStop, Directory
from hermes.structures.Graph import Graph
import json


with open("data/bus_routes.json", "r") as f:
    routes = json.load(f)

with open("data/bus_stops.json", "r") as f:
    stops = json.load(f)

d = Directory()
g = Graph()

for stop in stops:
    s = BusStop(*(stop.values()))
    d.addStop(s)
    g.addNode(s)

for i in range(len(routes) - 1):
    curr, next = routes[i], routes[i+1]
    if next["StopSequence"] > curr["StopSequence"]:
        dist = float("%.1f" % abs(next["Distance"] - curr["Distance"]))
        g.addRoute(
            d[curr["BusStopCode"]],
            d[next["BusStopCode"]],
            dist,
            curr["ServiceNo"]
        )

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(g._adjmap)

with open("adjlist", "wb") as f:
    pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)

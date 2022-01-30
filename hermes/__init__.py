import os
from flask import Flask, render_template, g, current_app
from .structures.Graph import BusGraph
from .structures.AStar import AStar
from .db import get_db

graph = None
astar = None


def init_graph() -> BusGraph:
    """
    Returns a graph containing all bus stops connected by their routes.

        Returns:
            temp_graph (BusGraph): BusGraph of Singapore bus routes.
    """
    temp_graph = BusGraph()
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM BusStops")
    for stop in cur:
        temp_graph.addStop(stop["BusStopCode"])

    cur.execute("SELECT * FROM BusRoutes")
    curr, prev = None, None
    for route in cur:
        curr = route

        if curr and prev and curr["StopSequence"] > prev["StopSequence"]:
            dist = float("%.1f" % abs(curr["Distance"] - prev["Distance"]))
            temp_graph.addRoute(prev["BusStopCode"],
                                curr["BusStopCode"],
                                dist,
                                prev["BusServiceNo"])

        prev = curr

    return temp_graph


def create_app(test_config=None):
    # create app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "hermes.sqlite"),
        TEMPLATES_AUTO_RELOAD=True
    )

    # ensure the instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # init db
    from . import db
    with app.app_context():
        db.init_db()
        db.build_db()

    # init data structures
    with app.app_context():
        global graph
        global astar
        graph = init_graph()
        astar = AStar(graph)

    # root page
    @app.route('/')
    def index():
        return render_template("index.html")

    # load blueprints
    from . import celeritas
    app.register_blueprint(celeritas.bp)

    return app

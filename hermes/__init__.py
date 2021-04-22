import os
from flask import Flask, render_template
from .structures import Graph

global graph
graph = Graph()


def init_graph():
    from .db import get_db
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM BusStops")
    for stop in cur:
        graph.addStop(stop["BusStopCode"])

    cur.execute("SELECT * FROM BusRoutes")
    for route in cur:
        curr = route

        if curr["StopSequence"] > prev["StopSequence"]:
            dist = float("%.1f" % abs(curr["Distance" - prev["StopSequence"]]))
            graph.addRoute(prev["BusStopCode"],
                           curr["BusStopCode"],
                           dist,
                           prev["BusServiceNo"])

        prev = curr


def create_app(test_config=None):
    # create app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "hermes.sqlite")
    )

    # ensure the instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # root page
    @app.route('/')
    def index():
        return render_template("index.html")

    from . import celeritas
    app.register_blueprint(celeritas.bp)

    # init
    from . import db
    db.init_app(app)

    with app.app_context():
        init_graph()

    return app

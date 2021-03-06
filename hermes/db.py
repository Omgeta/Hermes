import sqlite3
import json
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


def build_db():
    conn = get_db()
    cur = conn.cursor()

    with open("data/bus_stops.json", "r") as f:
        cur.executemany(
            '''
            INSERT INTO BusStops
            VALUES (:BusStopCode, :RoadName, :Description, :Latitude, :Longitude);
            ''', json.load(f)
        )

    with open("data/bus_services.json", "r") as f:
        cur.executemany(
            '''
            INSERT INTO BusServices
            VALUES (:ServiceNo, :Operator, :Direction, :Category, :OriginCode, :DestinationCode, :AM_Peak_Freq, :AM_Offpeak_Freq, :PM_Peak_Freq, :PM_Offpeak_Freq, :LoopDesc)
            ''', json.load(f)
        )

    with open("data/bus_routes.json", "r") as f:
        cur.executemany(
            '''
            INSERT INTO BusRoutes
            VALUES (NULL, :ServiceNo, :StopSequence, :BusStopCode, :Distance, :WD_FirstBus, :WD_LastBus, :SAT_FirstBus, :SAT_LastBus, :SUN_FirstBus, :SUN_LastBus);
            ''', json.load(f)
        )

    conn.commit()

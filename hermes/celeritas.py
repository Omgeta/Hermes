from math import sqrt
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from hermes.db import get_db
#from hermes import graph


bp = Blueprint("celeritas", __name__, url_prefix="/celeritas")


@bp.route("/")
def root():
    return render_template('celeritas/index.html')


@bp.route("process", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        src = request.form['src']
        dst = request.form['dst']
        db = get_db()
        error = None

        if not src:  # and if not valid
            error = "Invalid starting point."
        elif not dst:  # and if not valid
            error = "Invalid ending point."

        if error is None:
            print(src, dst)
            # run algo in C++ pathfind(src, dst, al)
            # parse data for results route
            return redirect(url_for("celeritas.result"))

        flash(error)
        return redirect(url_for("celeritas.root"))


@bp.route("result")
def result():
    return render_template('celeritas/result.html')


# def cost(a: str, b: str) -> float:
#     g = graph[a][b].getDistance()

#     conn = get_db()
#     cur = conn.cursor()
#     a_pos = cur.execute(
#         f"SELECT Latitude, Longitude FROM BusStops WHERE BusStopCode = {a}").fetchone()
#     b_pos = cur.execute(
#         f"SELECT Latitude, Longitude FROM BusStops WHERE BusStopCode = {b}").fetchone()
#     h = sqrt((a_pos[0] - b_pos[0])**2 + (a_pos[1] - b_pos[1])**2)

#     return g + h


# def astar(src, dst):
#     pass

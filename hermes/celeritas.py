from flask import Blueprint, flash, redirect, render_template, request, session, url_for, current_app
from hermes.structures import AStar
from hermes import graph, astar


bp = Blueprint("celeritas", __name__, url_prefix="/celeritas")


@bp.route("/")
def root():
    return render_template('celeritas/index.html')


@bp.route("process", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        src = request.form['src']
        dst = request.form['dst']
        error = None

        if not src or src not in graph:
            error = "Invalid starting point."
        elif not dst or dst not in graph:
            error = "Invalid ending point."
        elif src == dst:
            error = "Starting and ending points cannot be the same."

        if error is None:
            with current_app.app_context():
                total_path, total_route = astar.search(src, dst)
                global routes
                routes = [a + b for a, b in zip(total_path, total_route)]

            # create mapping for how many occurences of each road occur consecutively
            prev, curr = None, None
            global mapping
            mapping = {}
            for route in routes:
                curr = route[1]

                if curr not in mapping:
                    mapping[curr] = [1]
                elif curr in mapping:
                    if curr == prev:
                        mapping[curr][-1] += 1
                    else:
                        mapping[curr].extend([1])

                prev = curr

            return redirect(url_for("celeritas.result"))

        flash(error)
        return redirect(url_for("celeritas.root"))


@bp.route("result")
def result():
    return render_template('celeritas/result.html', routes=routes, mapping=mapping)

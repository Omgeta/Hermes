from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
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

        if not src:  # and if not valid
            error = "Invalid starting point."
        elif not dst:  # and if not valid
            error = "Invalid ending point."

        if error is None:

            with current_app.app_context():
                res = astar.search(src, dst)
                print(res)

            return redirect(url_for("celeritas.result"))

        flash(error)
        return redirect(url_for("celeritas.root"))


@bp.route("result")
def result():
    return render_template('celeritas/result.html')

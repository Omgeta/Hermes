import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from hermes.db import get_db

bp = Blueprint("celeritas", __name__, url_prefix="/celeritas")

@bp.route("/", methods=("GET", "POST"))
def root():
    if request.method == "POST":
        pass

    return render_template('celeritas/index.html')

@bp.route("result", methods=("GET"))
def result():
    pass
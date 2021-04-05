import os
from flask import Flask, render_template


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

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template("index.html")

    from . import db
    db.init_app(app)

    from . import celeritas
    app.register_blueprint(celeritas.bp)

    return app

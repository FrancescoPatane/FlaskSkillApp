from flask import render_template, jsonify, current_app
from pathlib import Path
from . import routes



@routes.route("/")
def main():
    renderPath = Path(__file__).parent.parent / "templates/index.html"
    return render_template(renderPath.name)

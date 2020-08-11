from flask import render_template, Blueprint
from pathlib import Path


routes = Blueprint('navigation_routes', __name__)




@routes.route("/")
def main():
    renderPath = Path(__file__).parent.parent / "templates/index.html"
    return render_template(renderPath.name)

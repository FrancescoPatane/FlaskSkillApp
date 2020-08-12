from flask import render_template, Blueprint
from pathlib import Path


routes = Blueprint('navigation_routes', __name__)




@routes.route("/")
def index_route():
    renderPath = Path(__file__).parent.parent / "templates/index.html"
    return render_template(renderPath.name)


@routes.route("/ledger/employees")
def employees_ledger():
    renderPath = Path(__file__).parent.parent / "templates/employees.html"
    return render_template(renderPath.name)

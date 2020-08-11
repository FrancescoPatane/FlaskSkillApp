from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .skill import *
from .employee import *
from .employeeskill import *

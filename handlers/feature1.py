from flask import Blueprint

bp = Blueprint('feature1', __name__, url_prefix='/feature1')

@bp.route('/', methods=['GET'])
def get():
	return "<p>Hello, World from Feature1!</p>"
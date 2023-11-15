from flask import Blueprint

bp = Blueprint('feature2', __name__, url_prefix='/feature2')

@bp.route('/', methods=['GET'])
def get():
	return "<p>Hello, World from Feature2!</p>"
from flask import Blueprint, request
from controllers.search_controller import handle_search

search_bp = Blueprint('search', __name__)

@search_bp.route('/<engine>', methods=['GET'])
def search(engine):
    query = request.args.get('query')
    start = request.args.get('start', type=int)
    return handle_search(engine, query, start)

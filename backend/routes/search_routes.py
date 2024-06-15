
from flask import Blueprint, request, jsonify
from controllers.search_controller import handle_search

search_bp = Blueprint('search', __name__)

@search_bp.route('/<browser>', methods=['GET'])
def search(browser):
    query = request.args.get('search_query')
    start = int(request.args.get('start', 0))
    if not query:
        return jsonify({"error": "search_query parameter is required"}), 400
    return handle_search(browser, query, start)

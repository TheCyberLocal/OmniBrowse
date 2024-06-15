
from flask import jsonify
from services.search_service import fetch_results

def handle_search(browser, query, start):
    try:
        results = fetch_results(browser, query, start)
        return jsonify(results)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

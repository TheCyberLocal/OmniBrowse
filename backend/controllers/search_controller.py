from services.search_service import fetch_results

def handle_search(engine, query, start):
    try:
        return fetch_results(engine, query, start)
    except ValueError as e:
        return {"error": str(e)}, 400

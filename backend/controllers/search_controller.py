from services.search_service import fetch_results

def handle_search(engine, query, start):
    try:
        results = fetch_results(engine, query, start)
        return results
    except ValueError as e:
        return {"error": str(e)}, 400

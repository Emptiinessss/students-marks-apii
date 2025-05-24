import json
import os

# Load student data from JSON file and build a dictionary: {name: marks}
students = {}
json_path = os.path.join(os.path.dirname(__file__), 'students.json')
with open(json_path, 'r') as f:
    data = json.load(f)
    for entry in data:
        students[entry['name']] = entry['marks']

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    # Handle preflight OPTIONS request for CORS
    if request.method == "OPTIONS":
        response.status_code = 204
        return ""

    # Get all 'name' query parameters (e.g., ?name=X&name=Y)
    names = request.args.getlist("name")
    # Fetch marks for each name, default to None if not found
    marks = [students.get(name, None) for name in names]

    response.headers["Content-Type"] = "application/json"
    return json.dumps({"marks": marks})

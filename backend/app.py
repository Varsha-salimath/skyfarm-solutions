"""SkyFarm Solutions – Flask backend API and static file server."""

import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from data import (
    calculate_space,
    check_soil,
    get_all_plants,
    get_tips,
    recommend_plants,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)


@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "css"), filename)


@app.route("/js/<path:filename>")
def serve_js(filename):
    return send_from_directory(os.path.join(FRONTEND_DIR, "js"), filename)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "app": "SkyFarm Solutions"})


@app.route("/api/plants", methods=["GET"])
def api_plants():
    return jsonify(get_all_plants())


@app.route("/api/plants/recommend", methods=["POST"])
def api_recommend_plants():
    data = request.get_json(silent=True) or {}
    sunlight = data.get("sunlight")
    season = data.get("season")
    soil = data.get("soil")

    if not all([sunlight, season, soil]):
        return jsonify({"error": "sunlight, season, and soil are required"}), 400

    plants = recommend_plants(sunlight, season, soil)
    return jsonify({"plants": plants, "count": len(plants)})


@app.route("/api/space/calculate", methods=["POST"])
def api_calculate_space():
    data = request.get_json(silent=True) or {}
    length = data.get("length")
    width = data.get("width")
    layout = data.get("layout", "rows")

    if length is None or width is None:
        return jsonify({"error": "length and width are required"}), 400

    try:
        length = float(length)
        width = float(width)
    except (TypeError, ValueError):
        return jsonify({"error": "length and width must be numbers"}), 400

    if length <= 0 or width <= 0:
        return jsonify({"error": "length and width must be positive"}), 400

    if layout not in ("rows", "grid", "containers"):
        return jsonify({"error": "layout must be rows, grid, or containers"}), 400

    return jsonify(calculate_space(length, width, layout))


@app.route("/api/soil/check", methods=["POST"])
def api_check_soil():
    data = request.get_json(silent=True) or {}
    plant_id = data.get("plant")
    soil = data.get("soil")

    if not plant_id or not soil:
        return jsonify({"error": "plant and soil are required"}), 400

    result = check_soil(plant_id, soil)
    if result is None:
        return jsonify({"error": "Unknown plant"}), 404

    return jsonify(result)


@app.route("/api/tips", methods=["GET"])
def api_tips():
    category = request.args.get("category", "all")
    return jsonify({"tips": get_tips(category)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

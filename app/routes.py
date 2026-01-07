
# app/routes.py
from flask import Blueprint, request, jsonify
from .api_client import login, request_daily_graph
from .symbols import symbols

main = Blueprint("main", __name__)

# ✅ Rota de saúde: sempre 200
@main.route("/healthz", methods=["GET"])
def healthz():
    return jsonify(status="ok"), 200

# Opcional: criar "/" para testes (não obrigatório para probes)
@main.route("/", methods=["GET"])
def root():
    return jsonify(service="flask-api-project"), 200

# ---- suas rotas atuais ----
session_id_global = {"sessionId": None}

@main.route("/login", methods=["GET"])
def login_route():
    response = login(msg_id=1)
    session_id_global["sessionId"] = response.get("sessionId")
    return jsonify({"status": "Login realizado", "sessionId": session_id_global["sessionId"]})

@main.route("/dailygraph", methods=["GET"])
def dailygraph_route():
    if not session_id_global["sessionId"]:
        return jsonify({"error": "Login não realizado"}), 401

    results = []
    for symbol in symbols:
        result = request_daily_graph(
            msg_id=2,
            session_id=session_id_global["sessionId"],
            symbol=symbol,
            date_from="2025-07-02",
            date_to="2025-07-02"
        )
        results.append({symbol: result})
    return jsonify(results)



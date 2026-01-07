import requests

API_URL = "https://strfeedhomoldci.cma.com.br/execute"
##API_URL = "https://strfeedrt06.cma.com.br/execute"
USERNAME = "STRFEEDVLI01"
PASSWORD = "Str@ViS3a"

def login(msg_id):
    payload = {
        "id": msg_id,
        "oms": {"ip": "0.0.0.0", "channel": "API", "language": "PT"},
        "advPsw": PASSWORD,
        "service": "m",
        "name": "LoginADVRequest",
        "sessionId": "",
        "transport": "Polling",
        "type": "s",
        "sync": True,
        "version": 1,
        "advUser": USERNAME
    }
    response = requests.post(API_URL, json=payload)
    return response.json()

def request_daily_graph(msg_id, session_id, symbol, date_from, date_to):
    payload = {
        "id": msg_id,
        "name": "DailyGraphRequest",
        "sessionId": session_id,
        "type": "c",
        "sync": True,
        "timeoutHandler": 120,
        "failActionType": "alert",
        "symbolId": {"sourceId": "100", "symbol": symbol},
        "dateFrom": date_from,
        "dateTo": date_to,
        "sign": False,
        "period": 1,
        "version": 3
    }
    response = requests.post(API_URL, json=payload)
    return response.json()


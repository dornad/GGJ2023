import json

ROOMS = []
CORRECT_ROOM = "sotano"

with open("./documents/cuartos.json") as cuartos_json_doc:
    ROOMS = json.load(cuartos_json_doc)

def get_rooms():
    """Gets all the rooms"""
    return ROOMS

def check_answer(answer):
    """Check the answer against the correct room"""
    return answer.lower() == CORRECT_ROOM
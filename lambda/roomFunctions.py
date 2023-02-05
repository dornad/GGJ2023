import json

ROOMS = []

with open("./documents/cuartos.json") as cuartos_json_doc:
    ROOMS = json.load(cuartos_json_doc)

def get_rooms():
    """Gets all the rooms"""
    return ROOMS
    
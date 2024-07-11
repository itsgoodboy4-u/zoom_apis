import json

def get_json(filepath):
    data = None
    with open(filepath,'r') as file:
        data = json.load(file)
    return [] if data is None else data

def write_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
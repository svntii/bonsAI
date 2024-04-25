import json

class JSONDict:
    def __init__(self, json_file):
        self.json_file = json_file
        try:
            with open(json_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save()

    def __delitem__(self, key):
        del self.data[key]
        self.save()

    def __contains__(self, key):
        return key in self.data

    def get(self, key, default=None):
        return self.data.get(key, default)

    def save(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def wipe(self):
        self.data = {}
        self.save()

    def __repr__(self):
        return repr(self.data)

database = JSONDict('history.json')

def pull_most_recent(conversation_id, count=5):
    return database[conversation_id][-count:]
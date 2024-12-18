import os
import json
from idlelib.editor import keynames


def read(file):
        with open(file, 'r') as f:
            return json.load(f)
def write(file, data):
    with open(file, 'w') as f:
     json.dump(data, f, indent=4)



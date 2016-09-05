import json
import sys
import os

dataset_path = sys.argv[1]
for line in open(dataset_path):
    try:
        jsonObj = json.loads(line)
    except ValueError:
        continue  # could not decode json line, skipping.
    try:
        print(jsonObj['id'])
    except KeyError:
        continue
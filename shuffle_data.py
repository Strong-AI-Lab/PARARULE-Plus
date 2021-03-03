import json_lines
import random
import json

dpoints = list()
filePath = './data/new_data/Depth5/Depth5.jsonl'
with open(filePath) as f:
    for l in json_lines.reader(f):
            dpoints.append(l)
random.shuffle(dpoints)


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

with open('./data/new_data/Depth5/PARARULE_Plus_Depth5_shuffled.jsonl', 'w') as f:
    for index in dpoints:
        json.dump(index, f, default=set_default)
        f.write('\n')
import json
# TODO решите задачу
with open('input.json', 'r') as file:
    data = json.load(file)

def task() -> float:
    sum = 0
    for pr in data:
        sum += pr["score"] * pr["weight"]
    return sum

print(round(task(),3))

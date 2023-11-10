import json


def task() -> float:
    with open('input.json') as f:
        json_data = json.load(f)

    composition_key = sum([i["score"] * i["weight"] for i in json_data])
    return composition_key


print(f"{task():.3f}")

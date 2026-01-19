# TODO решите задачу
def task() -> float:
    import json
    with open("input.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    total = 0.0
    for item in data:
        total += item["score"] * item["weight"]

    return round(total, 3)

print(task())

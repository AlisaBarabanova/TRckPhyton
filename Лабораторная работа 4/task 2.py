# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


with open(INPUT_FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=",")
    data = list(reader)

with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

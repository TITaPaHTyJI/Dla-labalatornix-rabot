import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        csv_file = csv.DictReader(f, delimiter=",", lineterminator="\n")
        python_str = [row for row in csv_file]
    jsons = json.dumps(python_str, indent=4)
    print(jsons, end='')

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

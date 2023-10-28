def find_common_participants(first_group, second_group, sep=","):
    group1 = first_group.split(sep)
    group2 = second_group.split(sep)
    general = list(set(group1).intersection(group2))
    general.sort()
    return general


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, sep='|')}")

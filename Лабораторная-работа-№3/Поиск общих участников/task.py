# TODO Напишите функцию find_common_participants
def find_common_participants(a1, a2, sep=','):
    participants_1 = a1.split(sep)
    participants_2 = a2.split(sep)

    common_participants = list(set(participants_1).intersection(participants_2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)

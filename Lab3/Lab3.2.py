# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, d=','):
    participants1 = group1.split(d)
    participants2 = group2.split(d)
    common_participants = set(participants1).intersection(participants2)
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

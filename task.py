# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep=","):
    p1=first_group.split(sep)
    p2=second_group.split(sep)
    return sorted(list(set(p1) & set(p2)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
#
print(find_common_participants(participants_first_group, participants_second_group, sep="|"))

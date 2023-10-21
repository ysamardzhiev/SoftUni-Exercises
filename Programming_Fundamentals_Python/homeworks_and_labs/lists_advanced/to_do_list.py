to_do_list = []

command = input()
while command != 'End':
    to_do_list.append(command)
    command = input()

sorted_notes = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
sorted_notes = [note.split('-')[1] for note in sorted_notes]
print(sorted_notes)

# SECOND OPTION
#
# to_do_list = ['0'] * 10
# command = input()
# while command != 'End':
#     task_priority = command.split('-')
#     index = int(task_priority[0]) - 1
#     note = task_priority[1]
#     to_do_list.pop(index)
#     to_do_list.insert(index, note)
#
#     command = input()
#
# sorted_list = [element for element in to_do_list if element != '0']
# print(sorted_list)
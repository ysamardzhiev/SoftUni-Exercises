number_of_electrons = int(input())

filled_shells = []

for shell in range(1, number_of_electrons + 1):
    max_electrons_in_a_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_in_a_shell:
        filled_shells.append(max_electrons_in_a_shell)
        number_of_electrons -= max_electrons_in_a_shell
        if number_of_electrons == 0:
            break
    else:
        filled_shells.append(number_of_electrons)
        break
print(filled_shells)
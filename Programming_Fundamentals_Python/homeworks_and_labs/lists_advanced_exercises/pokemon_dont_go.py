distances = [int(number) for number in input().split()]

all_removed_elements_sum = 0
while distances:
    index = int(input())
    if index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])
    elif index > len(distances) - 1:
        removed_element = distances.pop(len(distances) - 1)
        distances.append(distances[0])
    else:
        removed_element = distances.pop(index)
    all_removed_elements_sum += removed_element
    for element_index in range(len(distances)):
        if distances[element_index] <= removed_element:
            distances[element_index] += removed_element
        else:
            distances[element_index] -= removed_element
print(all_removed_elements_sum)
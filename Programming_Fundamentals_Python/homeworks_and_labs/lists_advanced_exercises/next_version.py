version = [int(number) for number in input().split('.')]

version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print('.'.join([str(number) for number in version]))


# SECOND OPTION
#
# software_version = input().split('.')
#
# version = int(''.join(software_version)) + 1
# updated_version = list(str(version))
# print('.'.join(updated_version))

software_version = input().split('.')

version = int(''.join(software_version)) + 1
updated_version = list(str(version))
print('.'.join(updated_version))

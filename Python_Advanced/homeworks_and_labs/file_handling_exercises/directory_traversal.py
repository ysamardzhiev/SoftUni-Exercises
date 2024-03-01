import os

path = os.path.join('..', 'file_handling_exercises')

files = {}

for file in os.listdir(path):
    if os.path.isdir(file):
        for file_name in os.listdir(file):
            if os.path.isdir():
                continue
                
            name, extension = file_name.split('.')
            files.setdefault(extension, [])
            files[extension].append(name)
    else:
        name, extension = file.split('.')
        files.setdefault(extension, [])
        files[extension].append(name)

sorted_files = sorted(files.items(), key=lambda x: x[0])
report_path = os.path.join('files', 'report.txt')

for extension, file_names in sorted_files:
    sorted_names = sorted(file_names)

    with open(report_path, 'a') as file:
        file.write(f'.{extension}\n')

        for file_name in sorted_names:
            file.write(f'- - - {file_name}.{extension}\n')

import os


def directory_traversal(dir_name):
    for file_name in os.listdir(dir_name):
        path = os.path.join(dir_name, file_name)

        if os.path.isfile(path):
            extension = file_name.split('.')[-1]
            extensions.setdefault(extension, [])
            extensions[extension].append(file_name)
        elif os.path.isdir(path):
            directory_traversal(path)


directory = input('Enter a directory: ')
extensions = {}

try:
    directory_traversal(directory)
except FileNotFoundError:
    print('No such directory found!')

sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in sorted_extensions:
    report_path = os.path.join(directory, 'files', 'report.txt')

    with open(report_path, 'a') as file:
        file.write(f'.{extension}\n')
        for current_file in sorted(files):
            file.write(f"- - - {current_file}\n")
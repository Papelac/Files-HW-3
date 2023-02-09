

files_information = {}

for i in range(3):
    file_name = f'{i+1}.txt'
    with open(file_name, 'rt', encoding='utf-8') as f:
        res = f.readlines()
        string_number = len(res)
        files_information[file_name] = string_number
    
print(files_information)
sorted_files_information = dict(sorted(files_information.items(), key=lambda item: item[1]))
print(sorted_files_information)

new_file_name = 'common_file.txt'
with open(new_file_name, 'w') as newfile:
    for file_name, string_number in sorted_files_information.items():
        print(file_name, string_number)
        newfile.write(f'{file_name}\n')
        newfile.write(f'{string_number}\n')
        with open(file_name, 'r', encoding='utf-8') as f:
            newfile.writelines(f.readlines())
            newfile.write('\n')


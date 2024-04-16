import subprocess

source = input(r'Enter source folder path: ')
target = input(r'Enter target folder path: ')
extension = input('enter the extension of the file: ')
input_file = input(r'Enter input file path: ')
# source = r'C:\Users\RAJESWARI\Desktop\cpfile_test\source'
# target = r'C:\Users\RAJESWARI\Desktop\cpfile_test\target'
# extension = 'png' 
# input_file = r'C:\Users\RAJESWARI\Desktop\cpfile_test'

with open(input_file, 'r') as file:
    input_data = file.read()
pic_list = [x for x in (input_data.split('\n')) if x]

tried = len(pic_list)
for each in pic_list:
    file_name = f'DSC_{each}.{extension}'
    copy_file = f"copy {file_name} {target}"
    res = subprocess.run(copy_file, shell=True,cwd=source, stdout=subprocess.PIPE)
    if res.stdout.decode('utf-8').strip() == '1 file(s) copied.':
        continue
    else:
        print(f'Copy operation failed for {file_name}')

file_count = f'dir /b /a-d {target}| find /c /v ""'
res = subprocess.run(file_count, shell=True,cwd=source, stdout=subprocess.PIPE)
num_files_in_target =res.stdout.decode('utf-8').strip()
print(f'Number of files tried to copy : {tried}\nNumber of files copied to target folder: {num_files_in_target}')

#open the file for read access
sample_file = open("textfile.txt", "r")
if sample_file.mode == 'r':
    contents = sample_file.read()
    print(contents)

file_lines = sample_file.readlines()
for line in file_lines:
    print(line)
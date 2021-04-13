filename = 'Text_files\learning _python.txt'

with open(filename) as file_object:
    lesson = file_object.read()
    print(lesson)

print('\n')

content = ''
for line in lesson:
    content += line

print(content)




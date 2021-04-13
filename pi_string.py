import math
filename = 'Text_files\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

while lines:
    geburstag = input('\tGeben Sie Ihren Geburtstag ein, in die ttmmjj: ')
    if geburstag in pi_string:
        print('\tDein Geburtstag befindet sich in den ersten millionen Zahlwerten von pi!')
        break
    else:
        print('\tDein Geburtstag befindet sich nicht in den ersten millionen Zahlwerten von pi.')
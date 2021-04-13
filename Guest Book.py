name = input('Geben Sie Ihren Namen ein: ')
while name:
    print('Hallo', name, 'schön dass Sie da sind')
    break
    name

filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    file_object.write(name + '\r\n')
    file_object.flush()
    file_object.close()
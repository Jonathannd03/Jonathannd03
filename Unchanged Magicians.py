#print('\nThese are the magicians  selected for the show:')

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    print('These are the great magicians:')
    greatMagicians = []
    for magician in magicians:
        full_name = 'the Great ' + magician
        greatMagicians.append(full_name)
    return greatMagicians

magicians = ['Val Valentino' ,'James Randi', 'David Blaine',
             'Lance Burton', 'Shin Lim']

make_great(magicians)

def make_album(artist_name, album_title, track=''):
    album = {}
    if track:
        album[artist_name] = album_title
        album[track] = ''
    else:
        album[artist_name] = album_title

    return album

while True:
    print('Enter the following infos please')
    print('\nPlease enter "q" or "quit" to quit')

    art_name = input('Enter the artist name: ')
    if art_name == 'q' or art_name == 'quit':
        break

    alb_title = input('Enter his album title: ')
    if alb_title == 'q' or alb_title == 'quit':
        break

    user_album = make_album(art_name,alb_title)
    print(user_album)




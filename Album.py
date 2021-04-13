def make_album(artist_name, album_title, track=''):
    album = {}
    if track:
        album[artist_name] = album_title
        album[track] = ''
    else:
        album[artist_name] = album_title

    return album


dictn = make_album('Fally ipupa', 'Tokoss')
print(dictn)

dictn = make_album('Yannick Ntumba', 'Emmanuel')
print(dictn)

dictn = make_album('Excel', 'Mafuta')
print(dictn)

dictn = make_album('Moise Mbiye', 'Triompe', 'track',)
print(dictn)

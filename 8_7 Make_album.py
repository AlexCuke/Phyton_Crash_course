def make_album(name_of_singer, name_of_album,tracks=None):
    album={'singer':name_of_singer,'album':name_of_album}
    if tracks is not None:
        album['tracks'] = tracks
    return album


print(make_album('Leningrad', 'WWW'))
print(make_album('Michael Jakson', 'Thriler'))
print(make_album('Queen', 'Innuende'))
print(make_album('Iron Maiden', 'Piece of Mind', tracks=8))


while 
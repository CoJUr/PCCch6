def make_album(artist, title, number_of_tracks=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist,
        'title': title

    }
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks

    return album


print(make_album("Michael Jackson", "Thriller", 10))
print(make_album("The Beatles", "Abbey Road", 9))
print(make_album("The Rolling Stones", "Exile on Main Street"))
print(make_album("The Rolling Stones", "Exile on Main Street", 12))
print(make_album("Janis Joplin", "Pearl"))
print(make_album("The Bare Naked Ladies", "Stunt"))


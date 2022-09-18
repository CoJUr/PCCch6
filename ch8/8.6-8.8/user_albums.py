def make_album(artist, title, number_of_tracks=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist,
        'title': title

    }
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks

    return album


while True:
    print("\nPlease tell me your favorite album by (artist) and (title): ")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)

    print(f"\nYour favorite album is {album}!")

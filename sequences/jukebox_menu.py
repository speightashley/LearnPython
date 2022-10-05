from nested_data import albums

SONG_LIST = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (Invalid choice exits)")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title, artist, year, songs))

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST]
    else:
        break

    print("Please choose your song")
    for index, (track_number, song) in enumerate(song_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        continue
    print("Playing {}".format(title))
    print("=" * 40)

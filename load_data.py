import os
from musicCollection import Artist as Artist
from musicCollection import Album as Album
from musicCollection import Song as Song

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)

            if new_artist is None:
                new_artist=Artist(artist_field)
            elif new_artist.name != artist_field:
                # save current new_artist and new_album
                new_artist.add_album(new_album)
                # add artist to list of all artists artist_list
                artist_list.append(new_artist)
                # create new artist
                new_artist=Artist(artist_field)
                new_album=None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # add current album to current artist
                new_artist.add_album(new_album)
                # create new album
                new_album=Album(album_field,year_field, new_artist)

            # for each line, create new song
            new_song = Song(song_field, new_artist)
            # add song to proper album
            new_album.add_song(new_song)

            # run after last line of file
            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)
    # return list of artist
    return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                 for new_song in new_album.tracks:
                     print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
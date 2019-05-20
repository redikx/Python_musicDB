class Song:
    """
    Class to represent single song
    Attributes:
        title (str) : title of the song
        artist (str) : name of the artist
        duration (int) : duration in seconds
    Methods:
        get_title() : return title of the song
    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent Album with artist and song list
        Attributes:
            name (str) : title of the album
            year (int) : year of the album
            artist (str) : artist of the album
            tracks(list[Song]) : list of Songs of the album
        Methods:
              add_song : Used to add song to Album
            """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        song_found = find_object(song,self.tracks)
        if song_found is None:
            song_found=Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position,song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, name, year, title):
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found=Album(name, year,title)
            self.add_album(album_found)
        else:
            print(name + " already added")
        album_found.add_song(title)


def find_object(field, object_list):
    """ Function to check if field exists in list, return field if Yes, None if No"""
    for item in object_list:
        if item.name == field:
            return item
    return None

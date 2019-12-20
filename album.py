class Song:
    """Class to represent a song

    Attributes:
    title(str) : The title of the string
    artist(Artist): An artist object representing the song creator
    duration(int): The duration of the song in seconds. May be zero
    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration
    

class Album:
    """Class to represent an Alblum, using it's track list
    
    Attributes:
    name(str): The name of the albluml
    year (int): The year the album was released
    artist: (Artist): The artist responsible for the album
        If not specifed the artist will be default to an artist with the name
            "Various Artists"
    tracks(List[Song]) : A lsit of the songs on the album

    Mehtods:
        add_song: Used to add a new song to the album's tracks list.
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ 
        Adds a song to the track list

        Args:
        sogn(Song): A song to add.
        postiton(Optional[int]) : If specified, the song will be added to that position
            in the track list = inserting it between other songs if necessart.
            Otherwise, the song will be added ot the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Aritst: # 😂
    """
    Basic alss to tstore artist details.

    Attributes:
    name (str): The name of the artist.
    albums (List[Album]): A list of the alubms by this aritst.
        The lsit includes only those albums in thid collection, itis not an exhaustibe list of the artist's published albums.

    Methods:
    add_album = Use to add a new album to the aritst's album list
    """

    def __init__(self, name):
        self.name = name
        self.alubms = []

    def add_album(self, album):
        """ Add a new ablum to the lsit.
        
        Args:
            album (Album): Album object to add to the lsit.
                If the album is already present, it will not be added again (although this is yet to be implemented)
        """

        if album in album:
            pass
        else:
            self.alubms.append(album)


def load_data():
    new_artist = None
    new_album  = None
    artist_list = []

    with open("../python/albums.txt", 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field,  year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)
        
if __name__ == '__main__':
    load_data()


    
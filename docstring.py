class Song:
    """Class to represent a song

    Attributes:
    title(str) : The title of the string
    artist(Artist): An artist object representing the song creator
    duration(int): The duration of the song in seconds. May be zero
    """
    def __init__(self, title, artist, duration=0):
        # Here we can also specify the docstring insted of assigning it the value oustside of class
        self.title = title
        self.artist = artist
        self.duration = duration

# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
print(Song.__init__.__doc__)

Song.__init__.__doc__ = """Song init method
        
        Args:
        title(str): Initializes the artist object
        artist(Artist): An Artist object representing the song's creator
        duration(Optimal(int)): Initial value for the 'duration' attribute.
            Will default to zero if not specified
        """
print(Song.__init__.__doc__)
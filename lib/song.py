class Song:
    # Class Attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count
        Song.add_song_to_count()
        
        # Add the genre and artist
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds genre to the genres list if it's not already present"""
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        """Adds artist to the artists list if it's not already present"""
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre_count dictionary to track number of songs in each genre"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist_count dictionary to track number of songs by each artist"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

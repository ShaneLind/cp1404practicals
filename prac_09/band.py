"""
CP1404 Practical
Band class file
"""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Construct a Band with an empty Musician list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians[0]}, {self.musicians[1]}, {self.musicians[2]}, {self.musicians[3]})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        play_output = ""
        for musician in self.musicians:
            if not musician.instruments:
                play_output += f"{musician.name} needs a musician! \n"
            else:
                play_output += f"{musician.name} is playing: {musician.instruments[0]} \n"
        return play_output

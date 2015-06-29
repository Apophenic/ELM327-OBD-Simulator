import random

class Switch(object):
    """An implementation of a switch statement for Python"""
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

def getrandhex():
    """Returns the last two characters of a random hex value
    (i.e. 0xAF would return AF)"""
    byte = hex(random.getrandbits(8))[2:].rjust(2, '0').upper()
    return byte


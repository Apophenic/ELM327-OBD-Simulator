import abc

class OBDResponse:
    """This super class defines logic for how the simulator instance
    should respond when a byte query is recieved"""
    __metaclass__ = abc.ABCMeta

    # Not every response uses all 4 bytes.
    byteA = byteB = byteC = byteD = None

    def __init__(self):
        pass

    @abc.abstractproperty
    def responsecode(self):
        """The response code bytes, represented as a string."""
        pass

    def getresponse(self):
        """A complete response will usually consist of the first two bytes
        representing the response code, and up to four bytes being used to relay the
        value"""
        response = self.responsecode()
        byteList = [self.byteA, self.byteB, self.byteC, self.byteD]

        for var in byteList:
            if var is not None:
                response += ' ' + var

        return response

    @abc.abstractmethod
    def getvalue(self):
        """Applies a response specific calculation to the response
        to return the actual value (i.e. for coolant temp, return Temperature
        in degrees C"""
        pass

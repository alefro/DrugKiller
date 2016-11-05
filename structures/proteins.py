
class Proteins:
    """

    """
    def __init__(self):
        self._sequence = ''

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, seq):
        self._sequence = seq

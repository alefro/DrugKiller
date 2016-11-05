from enum import Enum
from collections import namedtuple


AMINO_ACID = namedtuple('AMINO_ACID', 'name, symbol')


class AminoType(Enum):
    RNA = 'RNA'
    DNA = 'DNA'


class Nucleotides:
    """

    """
    def __init__(self, type=AminoType.DNA):
        self._adenine = AMINO_ACID(name='Adenine', symbol='A')
        self._thimine = AMINO_ACID(name='Thimine', symbol='T')
        self._guanine = AMINO_ACID(name='Guanine', symbol='G')
        if type == AminoType.RNA:
            self._uracil = AMINO_ACID(name='Uracil', symbol='U')
        else:
            self._cytosine = AMINO_ACID(name='Cytosine', symbol='C')

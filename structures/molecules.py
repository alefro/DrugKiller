
class Molecules:
    """

    """
    def __init__(self):
        self._smiles = ''

    @property
    def smiles(self):
        return self._smiles

    @smiles.setter
    def smiles(self, sm):
        self._smiles = sm

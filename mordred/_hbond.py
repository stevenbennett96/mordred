from rdkit.Chem import rdMolDescriptors

from ._base import Descriptor


class HBondBase(Descriptor):
    explicit_hydrogens = False

    @classmethod
    def preset(cls):
        yield cls()


class HBondAcceptor(HBondBase):
    r"""hydrogen bond acceptor descriptor(rdkit wrapper).

    :rtype: int
    """

    __slots__ = ()

    def __str__(self):
        return 'nHBAcc'

    def calculate(self, mol):
        return rdMolDescriptors.CalcNumHBA(mol)


class HBondDonor(HBondBase):
    r"""hydrogen bond donor descriptor(rdkit wrapper).

    :rtype: int
    """

    __slots__ = ()

    def __str__(self):
        return 'nHBDon'

    def calculate(self, mol):
        return rdMolDescriptors.CalcNumHBD(mol)

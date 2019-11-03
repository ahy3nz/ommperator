from simtk import openmm, unit
from ommperator import Ommperator, HarmonicBondForceOmmperator
from basetest import BaseTest

class TestBond(BaseTest):
    def test_parsing(self, ethane_system_topology):
        harmonic_bond = openmm.HarmonicBondForce()
        harmonic_bond.addBond(0, 1, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = HarmonicBondForceOmmperator(my_ommp, harmonic_bond, 0)

        assert my_bond_ommp.particle1 == harmonic_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle2 == harmonic_bond.getBondParameters(0)[1]
        assert my_bond_ommp.length == harmonic_bond.getBondParameters(0)[2]
        assert my_bond_ommp.k == harmonic_bond.getBondParameters(0)[3]

    def test_setting(self, ethane_system_topology):
        harmonic_bond = openmm.HarmonicBondForce()
        harmonic_bond.addBond(0, 1, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = HarmonicBondForceOmmperator(my_ommp, harmonic_bond, 0)
        my_bond_ommp.particle1 = 5
        my_bond_ommp.particle2 = 6
        my_bond_ommp.k = 100
        my_bond_ommp.length = 200

        assert my_bond_ommp.particle1 == harmonic_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 5
        assert my_bond_ommp.particle2 == harmonic_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 6
        assert my_bond_ommp.length == harmonic_bond.getBondParameters(0)[2]
        assert my_bond_ommp.k == harmonic_bond.getBondParameters(0)[3]

        my_bond_ommp.set_params(p1=100, p2=200,
                            k=300, length=400)

        assert my_bond_ommp.particle1 == harmonic_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 100
        assert my_bond_ommp.particle2 == harmonic_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 200
        assert my_bond_ommp.length == harmonic_bond.getBondParameters(0)[2]
        assert my_bond_ommp.k == harmonic_bond.getBondParameters(0)[3]


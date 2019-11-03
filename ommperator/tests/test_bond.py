import pytest
from simtk import openmm, unit
from ommperator import (Ommperator, HarmonicBondForceOmmperator, 
        CustomBondForceOmmperator)
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

    def test_modify_omm(self, ethane_system_topology):
        harmonic_bond = openmm.HarmonicBondForce()
        harmonic_bond.addBond(0, 1, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = HarmonicBondForceOmmperator(my_ommp, harmonic_bond, 0)

        harmonic_bond.setBondParameters(0, 1, 2, 20, 30)

        assert my_bond_ommp.particle1 == harmonic_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 1
        assert my_bond_ommp.particle2 == harmonic_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 2
        assert my_bond_ommp.length == harmonic_bond.getBondParameters(0)[2]
        assert my_bond_ommp.k == harmonic_bond.getBondParameters(0)[3]

class TestCustomBond(BaseTest):
    def test_parsing(self, ethane_system_topology):
        custom_bond = openmm.CustomBondForce('a+b*r')
        custom_bond.addPerBondParameter('a')
        custom_bond.addPerBondParameter('b')
        custom_bond.addBond(0, 1, (10, 20))
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = CustomBondForceOmmperator(my_ommp, custom_bond, 0)

        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]

    def test_setting(self, ethane_system_topology):
        custom_bond = openmm.CustomBondForce('a+b*r')
        custom_bond.addPerBondParameter('a')
        custom_bond.addPerBondParameter('b')
        custom_bond.addBond(0, 1, (10, 20))
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = CustomBondForceOmmperator(my_ommp, custom_bond, 0)

        my_bond_ommp.particle1 = 2
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 1
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]

        my_bond_ommp.particle2 = 3
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]

        my_bond_ommp.set_params(100, -1)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 100
        assert my_bond_ommp.parameters[1] == 20

        my_bond_ommp.set_params(-1, 200)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 100
        assert my_bond_ommp.parameters[1] == 200

        my_bond_ommp.set_params(1000, 2000)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 1000
        assert my_bond_ommp.parameters[1] == 2000

        my_bond_ommp.set_params(a=10)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 10
        assert my_bond_ommp.parameters[1] == 2000

        my_bond_ommp.set_params(b=20)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 10
        assert my_bond_ommp.parameters[1] == 20

        my_bond_ommp.set_params(a=100, b=200)
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 100
        assert my_bond_ommp.parameters[1] == 200

        with pytest.raises(ValueError):
            my_bond_ommp.set_params(100, 200, a=100, b=200)

    def test_modify_omm(self, ethane_system_topology):
        custom_bond = openmm.CustomBondForce('a+b*r')
        custom_bond.addPerBondParameter('a')
        custom_bond.addPerBondParameter('b')
        custom_bond.addBond(0, 1, (10, 20))
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_bond_ommp = CustomBondForceOmmperator(my_ommp, custom_bond, 0)

        custom_bond.setBondParameters(0, 2, 3, (100, 200))
        assert my_bond_ommp.particle1 == custom_bond.getBondParameters(0)[0]
        assert my_bond_ommp.particle1 == 2
        assert my_bond_ommp.particle2 == custom_bond.getBondParameters(0)[1]
        assert my_bond_ommp.particle2 == 3
        assert my_bond_ommp.parameters == custom_bond.getBondParameters(0)[2]
        assert my_bond_ommp.parameters[0] == 100
        assert my_bond_ommp.parameters[1] == 200


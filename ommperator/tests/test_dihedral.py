from simtk import openmm, unit
from ommperator import (Ommperator, PeriodicTorsionForceOmmperator, 
        RBTorsionForceOmmperator)
from basetest import BaseTest

class TestPeriodicTorsion(BaseTest):
    def test_parsing(self, ethane_system_topology):
        periodic_torsion = openmm.PeriodicTorsionForce()
        periodic_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = PeriodicTorsionForceOmmperator(my_ommp, periodic_torsion, 0)

        assert my_dih_ommp.particle1 == periodic_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle2 == periodic_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle3 == periodic_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle4 == periodic_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.n == periodic_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.phase == periodic_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.k == periodic_torsion.getTorsionParameters(0)[6]

    def test_setting(self, ethane_system_topology):
        periodic_torsion = openmm.PeriodicTorsionForce()
        periodic_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = PeriodicTorsionForceOmmperator(my_ommp, periodic_torsion, 0)
        my_dih_ommp.particle1 = 10
        my_dih_ommp.particle2 = 20
        my_dih_ommp.particle3 = 30
        my_dih_ommp.particle4 = 40
        my_dih_ommp.n == 50
        my_dih_ommp.phase == 60
        my_dih_ommp.k == 70

        assert my_dih_ommp.particle1 == periodic_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 10
        assert my_dih_ommp.particle2 == periodic_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 20
        assert my_dih_ommp.particle3 == periodic_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 30
        assert my_dih_ommp.particle4 == periodic_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 40
        assert my_dih_ommp.n == periodic_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.phase == periodic_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.k == periodic_torsion.getTorsionParameters(0)[6]

        my_dih_ommp.set_params(p1=100, p2=200, p3=300, p4=400,
                            n=500, phase=600, k=700)

        assert my_dih_ommp.particle1 == periodic_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 100
        assert my_dih_ommp.particle2 == periodic_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 200
        assert my_dih_ommp.particle3 == periodic_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 300
        assert my_dih_ommp.particle4 == periodic_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 400
        assert my_dih_ommp.n == periodic_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.phase == periodic_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.k == periodic_torsion.getTorsionParameters(0)[6]

    def test_modify_omm(self, ethane_system_topology):
        periodic_torsion = openmm.PeriodicTorsionForce()
        periodic_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = PeriodicTorsionForceOmmperator(my_ommp, periodic_torsion, 0)

        periodic_torsion.setTorsionParameters(0, 1, 2, 3, 4, 20, 30, 40)

        assert my_dih_ommp.particle1 == periodic_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 1
        assert my_dih_ommp.particle2 == periodic_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 2
        assert my_dih_ommp.particle3 == periodic_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 3
        assert my_dih_ommp.particle4 == periodic_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 4
        assert my_dih_ommp.n == periodic_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.phase == periodic_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.k == periodic_torsion.getTorsionParameters(0)[6]



class TestRBTorsion(BaseTest):
    def test_parsing(self, ethane_system_topology):
        rb_torsion = openmm.RBTorsionForce()
        rb_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30, 40, 50, 60)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = RBTorsionForceOmmperator(my_ommp, rb_torsion, 0)

        assert my_dih_ommp.particle1 == rb_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle2 == rb_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle3 == rb_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle4 == rb_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.c0 == rb_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.c1 == rb_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.c2 == rb_torsion.getTorsionParameters(0)[6]
        assert my_dih_ommp.c3 == rb_torsion.getTorsionParameters(0)[7]
        assert my_dih_ommp.c4 == rb_torsion.getTorsionParameters(0)[8]
        assert my_dih_ommp.c5 == rb_torsion.getTorsionParameters(0)[9]

    def test_setting(self, ethane_system_topology):
        rb_torsion = openmm.RBTorsionForce()
        rb_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30, 40, 50, 60)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = RBTorsionForceOmmperator(my_ommp, rb_torsion, 0)

        my_dih_ommp.particle1 = 10
        my_dih_ommp.particle2 = 20
        my_dih_ommp.particle3 = 30
        my_dih_ommp.particle4 = 40
        my_dih_ommp.c0 = 100
        my_dih_ommp.c1 = 200
        my_dih_ommp.c2 = 300
        my_dih_ommp.c3 = 400
        my_dih_ommp.c4 = 500
        my_dih_ommp.c5 = 600

        assert my_dih_ommp.particle1 == rb_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 10
        assert my_dih_ommp.particle2 == rb_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 20
        assert my_dih_ommp.particle3 == rb_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 30
        assert my_dih_ommp.particle4 == rb_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 40
        assert my_dih_ommp.c0 == rb_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.c1 == rb_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.c2 == rb_torsion.getTorsionParameters(0)[6]
        assert my_dih_ommp.c3 == rb_torsion.getTorsionParameters(0)[7]
        assert my_dih_ommp.c4 == rb_torsion.getTorsionParameters(0)[8]
        assert my_dih_ommp.c5 == rb_torsion.getTorsionParameters(0)[9]

        my_dih_ommp.set_params(p1=100, p2=200, p3=300, p4=400,
                c0=1000, c1=2000, c2=3000, c3=4000, c4=5000, c5=6000)

        assert my_dih_ommp.particle1 == rb_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 100
        assert my_dih_ommp.particle2 == rb_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 200
        assert my_dih_ommp.particle3 == rb_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 300
        assert my_dih_ommp.particle4 == rb_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 400
        assert my_dih_ommp.c0 == rb_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.c1 == rb_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.c2 == rb_torsion.getTorsionParameters(0)[6]
        assert my_dih_ommp.c3 == rb_torsion.getTorsionParameters(0)[7]
        assert my_dih_ommp.c4 == rb_torsion.getTorsionParameters(0)[8]
        assert my_dih_ommp.c5 == rb_torsion.getTorsionParameters(0)[9]

    def test_modify_omm(self, ethane_system_topology):
        rb_torsion = openmm.RBTorsionForce()
        rb_torsion.addTorsion(0, 1, 2, 3, 10, 20, 30, 40, 50, 60)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_dih_ommp = RBTorsionForceOmmperator(my_ommp, rb_torsion, 0)
        rb_torsion.setTorsionParameters(0, 1, 2, 3, 4, 20, 30, 40, 50, 60, 70)

        assert my_dih_ommp.particle1 == rb_torsion.getTorsionParameters(0)[0]
        assert my_dih_ommp.particle1 == 1
        assert my_dih_ommp.particle2 == rb_torsion.getTorsionParameters(0)[1]
        assert my_dih_ommp.particle2 == 2
        assert my_dih_ommp.particle3 == rb_torsion.getTorsionParameters(0)[2]
        assert my_dih_ommp.particle3 == 3
        assert my_dih_ommp.particle4 == rb_torsion.getTorsionParameters(0)[3]
        assert my_dih_ommp.particle4 == 4
        assert my_dih_ommp.c0 == rb_torsion.getTorsionParameters(0)[4]
        assert my_dih_ommp.c1 == rb_torsion.getTorsionParameters(0)[5]
        assert my_dih_ommp.c2 == rb_torsion.getTorsionParameters(0)[6]
        assert my_dih_ommp.c3 == rb_torsion.getTorsionParameters(0)[7]
        assert my_dih_ommp.c4 == rb_torsion.getTorsionParameters(0)[8]
        assert my_dih_ommp.c5 == rb_torsion.getTorsionParameters(0)[9]


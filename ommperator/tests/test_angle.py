from simtk import openmm, unit
from ommperator import Ommperator, HarmonicAngleForceOmmperator
from basetest import BaseTest

class TestAngle(BaseTest):
    def test_parsing(self, ethane_system_topology):
        harmonic_Angle = openmm.HarmonicAngleForce()
        harmonic_Angle.addAngle(0, 1, 2, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_Angle_ommp = HarmonicAngleForceOmmperator(my_ommp, harmonic_Angle, 0)

        assert my_Angle_ommp.particle1 == harmonic_Angle.getAngleParameters(0)[0]
        assert my_Angle_ommp.particle2 == harmonic_Angle.getAngleParameters(0)[1]
        assert my_Angle_ommp.particle3 == harmonic_Angle.getAngleParameters(0)[2]
        assert my_Angle_ommp.angle == harmonic_Angle.getAngleParameters(0)[3]
        assert my_Angle_ommp.k == harmonic_Angle.getAngleParameters(0)[4]

    def test_setting(self, ethane_system_topology):
        harmonic_Angle = openmm.HarmonicAngleForce()
        harmonic_Angle.addAngle(0, 1, 2, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_Angle_ommp = HarmonicAngleForceOmmperator(my_ommp, harmonic_Angle, 0)
        my_Angle_ommp.particle1 = 5
        my_Angle_ommp.particle2 = 6
        my_Angle_ommp.particle3 = 7
        my_Angle_ommp.angle = 100
        my_Angle_ommp.length = 200

        assert my_Angle_ommp.particle1 == harmonic_Angle.getAngleParameters(0)[0]
        assert my_Angle_ommp.particle1 == 5
        assert my_Angle_ommp.particle2 == harmonic_Angle.getAngleParameters(0)[1]
        assert my_Angle_ommp.particle2 == 6
        assert my_Angle_ommp.particle3 == harmonic_Angle.getAngleParameters(0)[2]
        assert my_Angle_ommp.particle3 == 7
        assert my_Angle_ommp.angle == harmonic_Angle.getAngleParameters(0)[3]
        assert my_Angle_ommp.k == harmonic_Angle.getAngleParameters(0)[4]

        my_Angle_ommp.set_params(p1=100, p2=200 ,p3=800, 
                            k=300, angle=400)

        assert my_Angle_ommp.particle1 == harmonic_Angle.getAngleParameters(0)[0]
        assert my_Angle_ommp.particle1 == 100
        assert my_Angle_ommp.particle2 == harmonic_Angle.getAngleParameters(0)[1]
        assert my_Angle_ommp.particle2 == 200
        assert my_Angle_ommp.particle3 == harmonic_Angle.getAngleParameters(0)[2]
        assert my_Angle_ommp.particle3 == 800
        assert my_Angle_ommp.angle == harmonic_Angle.getAngleParameters(0)[3]
        assert my_Angle_ommp.k == harmonic_Angle.getAngleParameters(0)[4]

    def test_modify_omm(self, ethane_system_topology):
        harmonic_Angle = openmm.HarmonicAngleForce()
        harmonic_Angle.addAngle(0, 1, 2, 10, 20)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_Angle_ommp = HarmonicAngleForceOmmperator(my_ommp, harmonic_Angle, 0)

        harmonic_Angle.setAngleParameters(0, 2, 3, 4, 20, 30)
        assert my_Angle_ommp.particle1 == harmonic_Angle.getAngleParameters(0)[0]
        assert my_Angle_ommp.particle1 == 2
        assert my_Angle_ommp.particle2 == harmonic_Angle.getAngleParameters(0)[1]
        assert my_Angle_ommp.particle2 == 3
        assert my_Angle_ommp.particle3 == harmonic_Angle.getAngleParameters(0)[2]
        assert my_Angle_ommp.particle3 == 4
        assert my_Angle_ommp.angle == harmonic_Angle.getAngleParameters(0)[3]
        assert my_Angle_ommp.k == harmonic_Angle.getAngleParameters(0)[4]


from ommperator import Ommperator
from basetest import BaseTest

class TestOmmperator(BaseTest):
    def test_parsing(self, ethane_system_topology):
        my_ommp = Ommperator(ethane_system_topology[0], 
                            ethane_system_topology[1])

        assert len(my_ommp.atoms) == 8
        assert len(my_ommp.bonds) == 7
        assert len(my_ommp.angles) == 12
        assert len(my_ommp.dihedrals) ==9 
        assert len(my_ommp.nonbonds) == 8

        assert len(my_ommp.bond_types) == 2
        assert len(my_ommp.angle_types) == 2
        assert len(my_ommp.dihedral_types) == 1
        assert len(my_ommp.nonbond_types) == 2

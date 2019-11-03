import pytest

class BaseTest:

    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()

    @pytest.fixture(autouse=True)
    def ethane_system_topology(self):
        from mbuild.examples import Ethane
        import foyer
        ethane = Ethane()
        structure = foyer.forcefields.load_OPLSAA().apply(ethane)
        system = structure.createSystem()
        topology = structure.topology
        for i, j in zip(structure.atoms, topology.atoms()):
            j.id = i.type
        return (system, topology)

    @pytest.fixture(autouse=True)
    def geometric_ethane_system_topology(self):
        from mbuild.examples import Ethane
        import foyer
        ethane = Ethane()
        structure = foyer.forcefields.load_OPLSAA().apply(ethane)
        structure.combining_rule = 'geometric'
        system = structure.createSystem()
        topology = structure.topology
        for i, j in zip(structure.atoms, topology.atoms()):
            j.id = i.type
        return (system, topology)

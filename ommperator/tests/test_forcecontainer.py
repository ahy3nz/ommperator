import simtk.unit as unit
from ommperator import Ommperator
from basetest import BaseTest

class TestForceContainer(BaseTest):
    def test_update_kwarg(self, ethane_system_topology):
        my_ommp = Ommperator(ethane_system_topology[0], 
                            ethane_system_topology[1])
        my_ommp.nonbond_types['opls_135'].update(sigma=5*unit.nanometer)
        for nonbond in my_ommp.nonbond_types['opls_135']:
            assert nonbond.sigma == 5*unit.nanometer

class TestCustomForceContainer(BaseTest):
    def test_update_kwarg(self, geometric_ethane_system_topology):
        my_ommp = Ommperator(geometric_ethane_system_topology[0], 
                            geometric_ethane_system_topology[1])
        my_ommp.custom_nonbond_types['opls_135'].update(sigma=5*unit.nanometer)
        param_index = my_ommp.custom_nonbonds[0].parameter_index['sigma']
        for nonbond in my_ommp.custom_nonbond_types['opls_135']:
            assert nonbond.parameters[param_index] == 5

    def test_update_arg(self, geometric_ethane_system_topology):
        my_ommp = Ommperator(geometric_ethane_system_topology[0], 
                            geometric_ethane_system_topology[1])
        my_ommp.custom_nonbond_types['opls_135'].update(
                10*unit.kilojoule_per_mole,
                5*unit.nanometer) 
        sigma_index = my_ommp.custom_nonbonds[0].parameter_index['sigma']
        epsilon_index = my_ommp.custom_nonbonds[0].parameter_index['epsilon']
        for nonbond in my_ommp.custom_nonbond_types['opls_135']:
            assert nonbond.parameters[sigma_index] == 5
            assert nonbond.parameters[epsilon_index] == 10


import pytest
from simtk import openmm, unit
from ommperator import (Ommperator, NonbondedForceOmmperator, 
        CustomNonbondedForceOmmperator)
from basetest import BaseTest
from utils import is_close

class TestNonbondedForce(BaseTest):
    def test_parsing(self, ethane_system_topology):
        nb_force = openmm.NonbondedForce()
        nb_force.addParticle(1, 2, 3)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_nb_ommp = NonbondedForceOmmperator(my_ommp, nb_force, 0)

        assert my_nb_ommp.charge == nb_force.getParticleParameters(0)[0]
        assert my_nb_ommp.sigma == nb_force.getParticleParameters(0)[1]
        assert my_nb_ommp.epsilon == nb_force.getParticleParameters(0)[2]
        
        assert is_close(my_nb_ommp.charge, 1*unit.elementary_charge)
        assert is_close(my_nb_ommp.sigma, 2*unit.nanometer)
        assert is_close(my_nb_ommp.epsilon, 3*unit.kilojoule_per_mole)

    def test_setting(self, ethane_system_topology):
        nb_force = openmm.NonbondedForce()
        nb_force.addParticle(1, 2, 3)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_nb_ommp = NonbondedForceOmmperator(my_ommp, nb_force, 0)

        my_nb_ommp.charge = 10*unit.elementary_charge
        my_nb_ommp.sigma = 20*unit.nanometer
        my_nb_ommp.epsilon = 30*unit.kilojoule_per_mole

        assert my_nb_ommp.charge == nb_force.getParticleParameters(0)[0]
        assert my_nb_ommp.sigma == nb_force.getParticleParameters(0)[1]
        assert my_nb_ommp.epsilon == nb_force.getParticleParameters(0)[2]

        assert is_close(my_nb_ommp.charge, 10*unit.elementary_charge)
        assert is_close(my_nb_ommp.sigma, 20*unit.nanometer)
        assert is_close(my_nb_ommp.epsilon, 30*unit.kilojoule_per_mole)

        my_nb_ommp.set_params(charge=100*unit.elementary_charge,
                                sigma=200*unit.nanometer,
                                epsilon=300*unit.kilojoule_per_mole)

        assert my_nb_ommp.charge == nb_force.getParticleParameters(0)[0]
        assert my_nb_ommp.sigma == nb_force.getParticleParameters(0)[1]
        assert my_nb_ommp.epsilon == nb_force.getParticleParameters(0)[2]

        assert is_close(my_nb_ommp.charge, 100*unit.elementary_charge)
        assert is_close(my_nb_ommp.sigma, 200*unit.nanometer)
        assert is_close(my_nb_ommp.epsilon, 300*unit.kilojoule_per_mole)

    def test_modify_omm(self, ethane_system_topology):
        nb_force = openmm.NonbondedForce()
        nb_force.addParticle(1, 2, 3)
        my_ommp = Ommperator(ethane_system_topology[0], ethane_system_topology[1])
        my_nb_ommp = NonbondedForceOmmperator(my_ommp, nb_force, 0)
        nb_force.setParticleParameters(0, 10, 20, 30)

        assert my_nb_ommp.charge == nb_force.getParticleParameters(0)[0]
        assert my_nb_ommp.sigma == nb_force.getParticleParameters(0)[1]
        assert my_nb_ommp.epsilon == nb_force.getParticleParameters(0)[2]
        
        assert is_close(my_nb_ommp.charge, 10*unit.elementary_charge)
        assert is_close(my_nb_ommp.sigma, 20*unit.nanometer)
        assert is_close(my_nb_ommp.epsilon, 30*unit.kilojoule_per_mole)



class TestCustomNonbondedForce(BaseTest):
    def test_parsing(self, geometric_ethane_system_topology):
        nb_force = openmm.CustomNonbondedForce('epsilon1*epsilon2*(sigr6^2-sigr6); sigr6=sigr2*sigr2*sigr2; '
                                        'sigr2=(sigc/r)^2; sigc=sigma1*sigma2')
        nb_force.addPerParticleParameter('epsilon')
        nb_force.addPerParticleParameter('sigma')
        nb_force.addParticle((1*unit.kilojoule_per_mole, 2*unit.nanometer))

        my_ommp = Ommperator(geometric_ethane_system_topology[0], 
                geometric_ethane_system_topology[1])
        my_nb_ommp = CustomNonbondedForceOmmperator(my_ommp, nb_force, 0)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.energy_function == nb_force.getEnergyFunction()
        assert my_nb_ommp.parameter_index['epsilon'] == 0
        assert my_nb_ommp.parameter_index['sigma'] == 1

    def test_setting(self, geometric_ethane_system_topology):
        nb_force = openmm.CustomNonbondedForce('epsilon1*epsilon2*(sigr6^2-sigr6); sigr6=sigr2*sigr2*sigr2; '
                                        'sigr2=(sigc/r)^2; sigc=sigma1*sigma2')
        nb_force.addPerParticleParameter('epsilon')
        nb_force.addPerParticleParameter('sigma')
        nb_force.addParticle((1*unit.kilojoule_per_mole, 2*unit.nanometer))

        my_ommp = Ommperator(geometric_ethane_system_topology[0], 
                geometric_ethane_system_topology[1])
        my_nb_ommp = CustomNonbondedForceOmmperator(my_ommp, nb_force, 0)

        my_nb_ommp.set_params(10*unit.kilojoule_per_mole, -1)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 10
        assert my_nb_ommp.parameters[1] == 2

        my_nb_ommp.set_params(-1, 20*unit.nanometer)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 10
        assert my_nb_ommp.parameters[1] == 20


        my_nb_ommp.set_params(epsilon=100*unit.kilojoule_per_mole)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 100
        assert my_nb_ommp.parameters[1] == 20

        my_nb_ommp.set_params(sigma=200*unit.nanometer)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 100
        assert my_nb_ommp.parameters[1] == 200

        my_nb_ommp.set_params(1000*unit.kilojoule_per_mole, 2000*unit.nanometer)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 1000
        assert my_nb_ommp.parameters[1] == 2000

        my_nb_ommp.set_params(epsilon=10000*unit.kilojoule_per_mole, 
                sigma=20000*unit.nanometer)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 10000
        assert my_nb_ommp.parameters[1] == 20000



        with pytest.raises(ValueError):
            my_nb_ommp.set_params(1,2,epsilon=3, sigma=4)

    def test_modify_omm(self, geometric_ethane_system_topology):
        nb_force = openmm.CustomNonbondedForce('epsilon1*epsilon2*(sigr6^2-sigr6); sigr6=sigr2*sigr2*sigr2; '
                                        'sigr2=(sigc/r)^2; sigc=sigma1*sigma2')
        nb_force.addPerParticleParameter('epsilon')
        nb_force.addPerParticleParameter('sigma')
        nb_force.addParticle((1*unit.kilojoule_per_mole, 2*unit.nanometer))

        nb_force.setParticleParameters(0, (10*unit.kilojoule_per_mole, 
                20*unit.nanometer))

        my_ommp = Ommperator(geometric_ethane_system_topology[0], 
                geometric_ethane_system_topology[1])
        my_nb_ommp = CustomNonbondedForceOmmperator(my_ommp, nb_force, 0)

        assert my_nb_ommp.parameters == nb_force.getParticleParameters(0)
        assert my_nb_ommp.parameters[0] == 10
        assert my_nb_ommp.parameters[1] == 20



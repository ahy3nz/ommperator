class NonbondedForceOmmperator:
    """ A NonbondedForceOmmperator refers to a single set of parameters
    within a NonbondedForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, parameter_index):
        self.ommperator = ommperator

        # OMM Nonbonded Bond Force Parameters
        self._force = force # The NonbondedForce object
        self._parameter_index = parameter_index # The index within the Force

    @property
    def force(self):
        return self._force

    @property
    def parameter_index(self):
        return self._parameter_index

    @property
    def charge(self):
        return self.force.getParticleParameters(self.parameter_index)[0]

    @property
    def sigma(self):
        return self.force.getParticleParameters(self.parameter_index)[1]

    @property
    def epsilon(self):
        return self.force.getParticleParameters(self.parameter_index)[2]

    @charge.setter
    def charge(self, q):
        self.force.setParticleParameters(self.parameter_index, q, 
                self.sigma, self.epsilon)
    
    @sigma.setter
    def sigma(self, sigma):
        self.force.setParticleParameters(self.parameter_index, self.charge,
                sigma, self.epsilon)

    @epsilon.setter
    def epsilon(self, epsilon):
        self.force.setParticleParameters(self.parameter_index, self.charge,
                self.sigma, epsilon)

    def set_params(self, charge=None, sigma=None, epsilon=None):
        if charge is None:
            charge = self.charge
        if sigma is None:
            sigma = self.sigma
        if epsilon is None:
            epsilon = self.epsilon

        self.force.setParticleParameters(self.parameter_index, charge,
                sigma, epsilon)

        return self.parameter_index

    def __repr__(self):

        return ("<NonbondedOmmperator, " +
                "i={}, ".format(self.parameter_index) +
                "charge={}, ".format(self.charge) +
                "sigma={}, ".format(self.sigma) +
                "epsilon={}>".format(self.epsilon))

class CustomNonbondedForceOmmperator:
    """ A CustomNonbondedForceOmmperator refers to a single set of parameters
    within a CustomNonbondedForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, parameter_index):
        self.ommperator = ommperator

        # OMM CustomNonbonded Bond Force Parameters
        self._force = force # The CustomNonbondedForce object
        self._parameter_index = parameter_index # The index within the Force

    @property
    def force(self):
        return self._force

    @property
    def parameter_index(self):
        return self._parameter_index

    @property
    def parameters(self):
        return self.force.getParticleParameters(self.parameter_index)

    @property
    def energy_function(self):
        return self.force.getEnergyFunction()

    def set_params(self, *args):
        original_parameters = self.parameters
        updated_args = [*args]
        for i, (orig, new) in enumerate(zip(original_parameters, args)):
            if new == -1: # If one of the args is -1, retain original parameter
                updated_args[i] = orig

        self.force.setParticleParameters(self.parameter_index,
                updated_args)

        return self.parameter_index

    def __repr__(self):
        return ("<CustomNonbondedOmmperator, " +
                "i={}, ".format(self.parameter_index) +
                "params={}>".format(self.parameters))


class NonbondedForceOmmperator:
    """ A NonbondedForceOmmperator refers to a single set of parameters
    within a NonbondedForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM Nonbonded Bond Force Parameters
        self._force = force # The NonbondedForce object
        self._force_index = force_index # The index within the Force

    @property
    def force(self):
        return self._force

    @property
    def force_index(self):
        return self._force_index

    @property
    def charge(self):
        return self.force.getParticleParameters(self.force_index)[0]

    @property
    def sigma(self):
        return self.force.getParticleParameters(self.force_index)[1]

    @property
    def epsilon(self):
        return self.force.getParticleParameters(self.force_index)[2]

    @charge.setter
    def charge(self, q):
        self.force.setParticleParameters(self.force_index, q, 
                self.sigma, self.epsilon)
    
    @sigma.setter
    def sigma(self, sigma):
        self.force.setParticleParameters(self.force_index, self.charge,
                sigma, self.epsilon)

    @epsilon.setter
    def epsilon(self, epsilon):
        self.force.setParticleParameters(self.force_index, self.charge,
                self.sigma, epsilon)

    def set_params(self, charge=None, sigma=None, epsilon=None):
        if charge is None:
            charge = self.charge
        if sigma is None:
            sigma = self.sigma
        if epsilon is None:
            epsilon = self.epsilon

        self.force.setParticleParameters(self.force_index, charge,
                sigma, epsilon)

        return self.force_index

    def __repr__(self):

        return ("<NonbondedOmmperator, " +
                "i={}, ".format(self.force_index) +
                "charge={}, ".format(self.charge) +
                "sigma={}, ".format(self.sigma) +
                "epsilon={}>".format(self.epsilon))

class CustomNonbondedForceOmmperator:
    """ A CustomNonbondedForceOmmperator refers to a single set of parameters
    within a CustomNonbondedForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM CustomNonbonded Bond Force Parameters
        self._force = force # The CustomNonbondedForce object
        self._force_index = force_index # The index within the Force

        # OpenMM refers to each particular particle's parameter
        # as ints within a tuple, but these particle parameters also have names
        self._parameter_index = self._parse_parameter_index(force)

    @property
    def force(self):
        return self._force

    @property
    def force_index(self):
        return self._force_index

    @property
    def parameters(self):
        return self.force.getParticleParameters(self.force_index)

    @property
    def energy_function(self):
        return self.force.getEnergyFunction()

    @property
    def parameter_index(self):
        return self._parameter_index

    def _parse_parameter_index(self, force):
        """ Relate the name of the parameter to its index 
        For example, if force.getPerParticleParmeters is a 2-tuple of
        (epsilon, sigma) parameters, whose names are ('epsilon', 'sigma'),
        then the parameter_index will yield {'epsilon':0, 'sigma':1} """
        parameter_index = {}
        for i in range(force.getNumPerParticleParameters()):
            param_name = force.getPerParticleParameterName(i)
            parameter_index[param_name] = i

        return parameter_index

    def set_params(self, *args, **kwargs):
        """ When setting customnonbondedforce params,
        they can be set either via args or kwargs
        For args, the order should be consistent with the Force's parameters.
            A value of -1 denotes using the original parameter
        For kwargs, the parameter_index is used to identify the
            index of the particular kwarg to set, and non-specified
            parameters will default to the original parameter """
        if len(kwargs) > 0 and len(args) > 0:
            raise ValueError("Can only pass one of args and kwargs")
        elif len(args) > 0:
            original_parameters = self.parameters
            updated_args = [*args]
            for i, (orig, new) in enumerate(zip(original_parameters, args)):
                if new == -1: # If one of the args is -1, retain original parameter
                    updated_args[i] = orig

            self.force.setParticleParameters(self.force_index,
                    updated_args)
        elif len(kwargs) > 0:
            original_parameters = self.parameters
            updated_args = [*original_parameters]
            for k, v in kwargs.items():
                index = self.parameter_index[k]
                updated_args[index] = v
            
            self.force.setParticleParameters(self.force_index,
                    updated_args)

        return self.force_index

    def __repr__(self):
        return ("<CustomNonbondedOmmperator, " +
                "i={}, ".format(self.force_index) +
                "params={}>".format(self.parameters))


class HarmonicBondForceOmmperator():
    """ A HarmonicBondForceOmmperator refers to a single set of parameters
    within a HarmonicBondForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM Harmonic Bond Force Parameters
        self._force = force # The HarmonicBondForce object
        self._force_index = force_index # The index within the Force


    @property
    def force(self):
        return self._force

    @property
    def force_index(self):
        return self._force_index

    @property
    def particle1(self):
        return self.force.getBondParameters(self.force_index)[0]

    @property
    def particle2(self):
        return self.force.getBondParameters(self.force_index)[1]

    @property
    def length(self):
        return self.force.getBondParameters(self.force_index)[2]

    @property
    def k(self):
        return self.force.getBondParameters(self.force_index)[3]

    @length.setter
    def length(self, length):
        self.force.setBondParameters(self.force_index, self.particle1,
                self.particle2, length, self.k)

    @k.setter
    def k(self, k): 
        self.force.setBondParameters(self.force_index, self.particle1,
                self.particle2, self.length, k)

    @particle1.setter
    def particle1(self, particle1):
        self.force.setBondParameters(self.force_index, particle1,
                self.particle2, self.length, self.k)

    @particle2.setter
    def particle2(self, particle2):
        self.force.setBondParameters(self.force_index, self.particle1,
                particle2, self.length, self.k)

    def set_params(self, p1=None, p2=None, length=None, k=None):
        if p1 is None:
            p1 = self.particle1
        if p2 is None:
            p2 = self.particle2
        if length is None:
            length = self.length
        if k is None:
            k = self.k

        self.force.setBondParameters(self.force_index,
                p1, p2, length, k)

        return self.force_index

    def __repr__(self):
        return ("<HarmonicBondOmmperator, " +
                "i={}, ".format(self.force_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "l={}, ".format(self.length) + 
                "k={}>".format(self.k))

class CustomBondForceOmmperator:
    """ A CustomBondForceOmmperator refers to a single set of parameters
    within a CustomBondForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM CustomBond Force Parameters
        self._force = force # The CustomBondForce object
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
    def particle1(self):
        return self.force.getBondParameters(self.force_index)[0]

    @property
    def particle2(self):
        return self.force.getBondParameters(self.force_index)[1]

    @property
    def parameters(self):
        return self.force.getBondParameters(self.force_index)[2]

    @property
    def energy_function(self):
        return self.force.getEnergyFunction()

    @property
    def parameter_index(self):
        return self._parameter_index

    @particle1.setter
    def particle1(self, p1):
        original_parameters = self.force.getBondParameters(self.force_index)
        original_parameters[0] = p1
        self.force.setBondParameters(self.force_index, *original_parameters)
    
    @particle2.setter
    def particle2(self, p2):
        original_parameters = self.force.getBondParameters(self.force_index)
        original_parameters[1] = p2
        self.force.setBondParameters(self.force_index, *original_parameters)

    def _parse_parameter_index(self, force):
        """ Relate the name of the parameter to its index 
        For example, if force.getPerBondParmeters is a 2-tuple of
        (epsilon, sigma) parameters, whose names are ('epsilon', 'sigma'),
        then the parameter_index will yield {'epsilon':0, 'sigma':1} """
        parameter_index = {}
        for i in range(force.getNumPerBondParameters()):
            param_name = force.getPerBondParameterName(i)
            parameter_index[param_name] = i

        return parameter_index

    def set_params(self, *args, **kwargs):
        """ When setting customnbondforce params,
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

            self.force.setBondParameters(self.force_index,
                    self.particle1, self.particle2,
                    updated_args)
        elif len(kwargs) > 0:
            original_parameters = self.parameters
            updated_args = [*original_parameters]
            for k, v in kwargs.items():
                index = self.parameter_index[k]
                updated_args[index] = v
            
            self.force.setBondParameters(self.force_index,
                    self.particle1, self.particle2,
                    updated_args)

        return self.force_index

    def __repr__(self):
        return ("<CustomBondForceOmmperator, " +
                "i={}, ".format(self.force_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "params={}>".format(self.parameters))


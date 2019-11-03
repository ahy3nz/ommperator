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

    def __repr__(self):
        return ("<NonbondedOmmperator, " +
                "i={}, ".format(self.parameter_index) +
                "charge={}, ".format(self.charge) +
                "sigma={}, ".format(self.sigma) +
                "epsilon={}>".format(self.epsilon))


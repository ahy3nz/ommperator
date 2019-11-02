class HarmonicBondForceOmmperator():
    """ A HarmonicBondForceOmmperator refers to a single set of parameters
    within a HarmonicBondForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, parameter_index):
        self.ommperator = ommperator

        # OMM Harmonic Bond Force Parameters
        self._force = force # The HarmonicBondForce object
        self._parameter_index = parameter_index # The index within the Force


    @property
    def force(self):
        return self._force

    @property
    def parameter_index(self):
        return self._parameter_index

    @property
    def particle1(self):
        return self.force.getBondParameters(self.parameter_index)[0]

    @property
    def particle2(self):
        return self.force.getBondParameters(self.parameter_index)[1]

    @property
    def length(self):
        return self.force.getBondParameters(self.parameter_index)[2]

    @property
    def k(self):
        return self.force.getBondParameters(self.parameter_index)[3]

    @length.setter
    def length(self, length):
        self.force.setBondParameters(self.parameter_index, self.particle1,
                self.particle2, length, self.k)

    @k.setter
    def k(self, k): 
        self.force.setBondParameters(self.parameter_index, self.particle1,
                self.particle2, self.length, k)

    @particle1.setter
    def particle1(self, particle1):
        self.force.setBondParameters(self.parameter_index, particle1,
                self.particle2, self.length, self.k)

    @particle2.setter
    def particle2(self, particle2):
        self.force.setBondParameters(self.parameter_index, self.particle1,
                particle2, self.length, self.k)

    def set_params(self, p1=None, p2=None, l=None, k=None):
        if p1 is None:
            p1 = self.particle1
        if p2 is None:
            p2 = self.particle2
        if l is None:
            l = self.length
        if k is None:
            k = self.k

        self.force.setBondParameters(self.parameter_index,
                p1, p2, l, k)

        return self.parameter_index

    def __repr__(self):
        return ("<HarmonicBondOmmperator, " +
                "i={}, ".format(self.parameter_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "l={}, ".format(self.length) + 
                "k={}>".format(self.k))
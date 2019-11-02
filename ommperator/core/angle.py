class HarmonicAngleForceOmmperator():
    """ A HarmonicAngleForceOmmperator refers to a single set of parameters
    within a HarmonicAngleForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, parameter_index):
        self.ommperator = ommperator

        # OMM Harmonic Angle Force Parameters
        self._force = force # The HarmonicAngleForce object
        self._parameter_index = parameter_index # The index within the Force


    @property
    def force(self):
        return self._force

    @property
    def parameter_index(self):
        return self._parameter_index

    @property
    def particle1(self):
        return self.force.getAngleParameters(self.parameter_index)[0]

    @property
    def particle2(self):
        return self.force.getAngleParameters(self.parameter_index)[1]

    @property
    def particle3(self):
        return self.force.getAngleParameters(self.parameter_index)[2]

    @property
    def angle(self):
        return self.force.getAngleParameters(self.parameter_index)[3]

    @property
    def k(self):
        return self.force.getAngleParameters(self.parameter_index)[4]

    @angle.setter
    def angle(self, angle):
        self.force.setAngleParameters(self.parameter_index, self.particle1,
                self.particle2, self.particle3, angle, self.k)

    @k.setter
    def k(self, k): 
        self.force.setAngleParameters(self.parameter_index, self.particle1,
                self.particle2, self.particle3, self.angle, k)

    @particle1.setter
    def particle1(self, particle1):
        self.force.setAngleParameters(self.parameter_index, particle1,
                self.particle2, self.particle3, self.angle, self.k)

    @particle2.setter
    def particle2(self, particle2):
        self.force.setAngleParameters(self.parameter_index, self.particle1,
                particle2, self.particle3, self.angle, self.k)

    @particle3.setter
    def particle3(self, particle3):
        self.force.setAngleParameters(self.parameter_index, self.particle1,
                self.particle2, particle3, self.angle, self.k)

    def set_params(self, p1=None, p2=None, p3=None, angle=None, k=None):
        if p1 is None:
            p1 = self.particle1
        if p2 is None:
            p2 = self.particle2
        if p3 is None:
            p3 = self.particle3
        if angle is None:
            angle = self.angle
        if k is None:
            k = self.k

        self.force.setAngleParameters(self.parameter_index,
                p1, p2, p3, angle, k)

        return self.parameter_index

    def __repr__(self):
        return ("<HarmonicAngleOmmperator, " +
                "i={}, ".format(self.parameter_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "p3={}, ".format(self.particle3) +
                "angle={}, ".format(self.angle) + 
                "k={}>".format(self.k))

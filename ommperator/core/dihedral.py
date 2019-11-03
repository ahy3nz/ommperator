class RBTorsionForceOmmperator():
    """ A RBTorsionForceOmmperator refers to a single set of parameters
    within a RBTorsionForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM RB Torsion Force Parameters
        self._force = force # The RBTorsionForce object
        self._force_index = force_index # The index within the Force


    @property
    def force(self):
        return self._force

    @property
    def force_index(self):
        return self._force_index

    @property
    def particle1(self):
        return self.force.getTorsionParameters(self.force_index)[0]

    @property
    def particle2(self):
        return self.force.getTorsionParameters(self.force_index)[1]

    @property
    def particle3(self):
        return self.force.getTorsionParameters(self.force_index)[2]

    @property
    def particle4(self):
        return self.force.getTorsionParameters(self.force_index)[3]

    @property
    def c0(self):
        return self.force.getTorsionParameters(self.force_index)[4]

    @property
    def c1(self):
        return self.force.getTorsionParameters(self.force_index)[5]

    @property
    def c2(self):
        return self.force.getTorsionParameters(self.force_index)[6]

    @property
    def c3(self):
        return self.force.getTorsionParameters(self.force_index)[7]

    @property
    def c4(self):
        return self.force.getTorsionParameters(self.force_index)[8]

    @property
    def c5(self):
        return self.force.getTorsionParameters(self.force_index)[9]

    @c0.setter
    def c0(self, c0):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                c0, self.c1, self.c2, self.c3, self.c4, self.c5)

    @c1.setter
    def c1(self, c1):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, c1, self.c2, self.c3, self.c4, self.c5)

    @c2.setter
    def c2(self, c2):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, self.c1, c2, self.c3, self.c4, self.c5)

    @c3.setter
    def c3(self, c3):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, self.c1, self.c2, c3, self.c4, self.c5)

    @c4.setter
    def c4(self, c4):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, self.c1, self.c2, self.c3, c4, self.c5)

    @c5.setter
    def c5(self, c5):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, self.c1, self.c2, self.c3, self.c4, c5)

    @particle1.setter
    def particle1(self, particle1):
        self.force.setTorsionParameters(self.force_index, particle1,
                self.particle2, self.particle3, self.particle4,
                self.c0, self.c1, self.c2, self.c3, self.c4, self.c5)

    @particle2.setter
    def particle2(self, particle2):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                particle2, self.particle3, self.particle4,
                self.c0, self.c1, self.c2, self.c3, self.c4, self.c5)

    @particle3.setter
    def particle3(self, particle3):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, particle3, self.particle4,
                self.c0, self.c1, self.c2, self.c3, self.c4, self.c5)

    @particle4.setter
    def particle4(self, particle4):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, particle4,
                self.c0, self.c1, self.c2, self.c3, self.c4, self.c5)

    def set_params(self, p1=None, p2=None, p3=None, p4=None,
            c0=None, c1=None, c2=None, c3=None, c4=None, c5=None):
        if p1 is None:
            p1 = self.particle1
        if p2 is None:
            p2 = self.particle2
        if p3 is None:
            p3 = self.particle3
        if p4 is None:
            p4 = self.particle4
        if c0 is None:
            c0 = self.c0
        if c1 is None:
            c1 = self.c1
        if c2 is None:
            c2 = self.c2
        if c3 is None:
            c3 = self.c3
        if c4 is None:
            c4 = self.c4
        if c5 is None:
            c5 = self.c5

        self.force.setTorsionParameters(self.force_index,
                p1, p2, p3, p4, c0, c1, c2, c3, c4, c5)

        return self.force_index

    def __repr__(self):
        return ("<RBTorsionOmmperator, " +
                "i={}, ".format(self.force_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "p3={}, ".format(self.particle3) +
                "p4={}, ".format(self.particle4) +
                "c0={}, ".format(self.c0) +
                "c1={}, ".format(self.c1) +
                "c2={}, ".format(self.c2) +
                "c3={}, ".format(self.c3) +
                "c4={}, ".format(self.c4) +
                "c5={}>".format(self.c5))

class PeriodicTorsionForceOmmperator():
    """ A PeriodicTorsionForceOmmperator refers to a single set of parameters
    within a PeriodicTorsionForce
    
    Most properties access the underlying Force object
    Most setters modify the underlying Force object,
     """
    def __init__(self, ommperator, force, force_index):
        self.ommperator = ommperator

        # OMM Periodic Torsion Force Parameters
        self._force = force # The PeriodicTorsionForce object
        self._force_index = force_index # The index within the Force


    @property
    def force(self):
        return self._force

    @property
    def force_index(self):
        return self._force_index

    @property
    def particle1(self):
        return self.force.getTorsionParameters(self.force_index)[0]

    @property
    def particle2(self):
        return self.force.getTorsionParameters(self.force_index)[1]

    @property
    def particle3(self):
        return self.force.getTorsionParameters(self.force_index)[2]

    @property
    def particle4(self):
        return self.force.getTorsionParameters(self.force_index)[3]

    @property
    def n(self):
        return self.force.getTorsionParameters(self.force_index)[4]

    @property
    def phase(self):
        return self.force.getTorsionParameters(self.force_index)[5]

    @property
    def k(self):
        return self.force.getTorsionParameters(self.force_index)[6]

    @n.setter
    def n(self, n):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                n, self.phase, self.k)

    @phase.setter
    def phase(self, phase):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.n, phase, self.k)

    @k.setter
    def k(self, k): 
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, self.particle4,
                self.n, self.phase, k)

    @particle1.setter
    def particle1(self, particle1):
        self.force.setTorsionParameters(self.force_index, particle1,
                self.particle2, self.particle3, self.particle4,
                self.n, self.phase, self.k)

    @particle2.setter
    def particle2(self, particle2):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                particle2, self.particle3, self.particle4,
                self.n, self.phase, self.k)

    @particle3.setter
    def particle3(self, particle3):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, particle3, self.particle4,
                self.n, self.phase, self.k)

    @particle4.setter
    def particle4(self, particle4):
        self.force.setTorsionParameters(self.force_index, self.particle1,
                self.particle2, self.particle3, particle4,
                self.n, self.phase, self.k)

    def set_params(self, p1=None, p2=None, p3=None, p4=None,
            n=None, phase=None, k=None):
        if p1 is None:
            p1 = self.particle1
        if p2 is None:
            p2 = self.particle2
        if p3 is None:
            p3 = self.particle3
        if p4 is None:
            p4 = self.particle4
        if n is None:
            n = self.n
        if phase is None:
            phase = self.phase
        if k is None:
            k = self.k

        self.force.setTorsionParameters(self.force_index,
                p1, p2, p3, p4, n, phase, k)

        return self.force_index

    def __repr__(self):
        return ("<PeriodicTorsionOmmperator, " +
                "i={}, ".format(self.force_index) +
                "p1={}, ".format(self.particle1) +
                "p2={}, ".format(self.particle2) +
                "p3={}, ".format(self.particle3) +
                "p4={}, ".format(self.particle4) +
                "n={}, ".format(self.n) +
                "phase={}, ".format(self.phase) + 
                "k={}>".format(self.k))

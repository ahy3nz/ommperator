import simtk.openmm as openmm

from .forcecontainer import ForceContainer
from .bond import HarmonicBondForceOmmperator
from .angle import HarmonicAngleForceOmmperator
from .dihedral import (PeriodicTorsionForceOmmperator,
                        RBTorsionForceOmmperator)
from .nonbond import NonbondedForceOmmperator


class AtomOmmperator():
    """ An AtomOmmperator refers to the Topology atom with
    additional information 
    
    Parameters
    ---------
    ommperator : ommperator.Ommperator
    index : int
        atomic index
    atom : openmm.Atom
    residue :
    bonds :
    angles : 
    dihedrals : """
    def __init__(self, ommperator, atom, 
            bonds=None, angles=None, dihedrals=None, nonbonds=None):
        self._ommperator = ommperator
        self._atom = atom

        if bonds is None:
            bonds = ForceContainer()
        self._bonds = bonds
        if angles is None:
            angles = ForceContainer()
        self._angles = angles
        if dihedrals is None:
            dihedrals = ForceContainer()
        self._dihedrals = dihedrals
        if nonbonds is None:
            nonbonds = ForceContainer()
        self._nonbonds = nonbonds

        for force in self.ommperator.system.getForces():
            if isinstance(force, openmm.HarmonicBondForce):
                self._identify_harmonic_bonds(force)
            if isinstance(force, openmm.HarmonicAngleForce):
                self._identify_harmonic_angles(force)
            if isinstance(force, openmm.RBTorsionForce):
                self._identify_RB_torsions(force)
            if isinstance(force, openmm.PeriodicTorsionForce):
                self._identify_periodic_torsions(force)
            if isinstance(force, openmm.NonbondedForce):
                self._identify_nonbonds(force)

    @property
    def bonds(self):
        return self._bonds

    @property
    def angles(self):
        return self._angles

    @property
    def dihedrals(self):
        return self._dihedrals

    @property
    def nonbonds(self):
        return self._nonbonds

    @property
    def ommperator(self):
        return self._ommperator

    @property
    def atom(self):
        return self._atom

    @property
    def index(self):
        return self.atom.index

    @property
    def residue(self):
        return self.atom.residue

    @property
    def bond_partners(self):
        return self.atom.bond_partners

    @property
    def name(self):
        return self.atom.name
    
    @property
    def id(self):
        return self.atom.id

    @property
    def name(self):
        return self.atom.name

    def _identify_harmonic_bonds(self, force):
        for i in range(force.getNumBonds()):
            p1, p2, length, k = force.getBondParameters(i)
            if self.index in [p1, p2]:
                to_add = HarmonicBondForceOmmperator(self, force, i)
                self.bonds.append(to_add)

    def _identify_harmonic_angles(self, force):
        for i in range(force.getNumAngles()):
            p1, p2, p3, angle, k = force.getAngleParameters(i)
            if self.index in [p1, p2, p3]:
                to_add = HarmonicAngleForceOmmperator(self, force, i)
                self.angles.append(to_add)

    def _identify_periodic_torions(self, force):
        for i in range(force.getNumTorsions()):
            p1, p2, p3, p4, n, phase, k = force.getTorsionParameters(i)
            if self.index in [p1,p2,p3,p4]:
                to_add = PeriodicTorsionForceOmmperator(self, force, i)
                self.dihedrals.append(to_add)

    def _identify_RB_torsions(self, force):
        for i in range(force.getNumTorsions()):
            p1, p2, p3, p4, c0, c1, c2, c3, c4, c5  = force.getTorsionParameters(i)
            if self.index in [p1, p2, p3, p4]:
                to_add = RBTorsionForceOmmperator(self, force, i)
                self.dihedrals.append(to_add)

    def _identify_nonbonds(self, force):
        to_add = NonbondedForceOmmperator(self, force, self.index)
        self.nonbonds.append(to_add)

    def __repr__(self):
        return ("<AtomOmmperator, " +
                "i={}, ".format(self.index) +
                "name={}, ".format(self.name) +
                "id={}, ".format(self.id) +
                "res={}>".format(self.residue)
                )



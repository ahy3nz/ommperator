import simtk.openmm as openmm
from .bond import HarmonicBondForceOmmperator
from .angle import HarmonicAngleForceOmmperator
from .dihedral import PeriodicTorsionForceOmmperator, RBTorsionForceOmmperator
from .forcecontainer import ForceContainer

class Ommperator:
    """ An interface to operate on openmm systems and topologies """
    def __init__(self, system, topology):
        self.system = system
        self.topology = topology

        self.bonds = {}
        self.angles = {}
        self.dihedrals = {}

        for force in self.system.getForces():
            if isinstance(force, openmm.HarmonicBondForce):
                self._parse_harmonic_bonds(force)
            if isinstance(force, openmm.HarmonicAngleForce):
                self._parse_harmonic_angles(force)
            if isinstance(force, openmm.PeriodicTorsionForce):
                self._parse_periodic_torsions(force)
            if isinstance(force, openmm.RBTorsionForce):
                self._parse_RB_torsions(force)


    @property
    def atoms(self):
        return [*self.topology.atoms()]

    def _parse_harmonic_bonds(self, force):
        """ For every set of parameters within the HarmonicBondForce,
        create an associated HarmonicBondOmmperator """
        for i in range(force.getNumBonds()):
            p1, p2, length, k = force.getBondParameters(i)
            to_add = HarmonicBondForceOmmperator(self, force, i)
            first, second = sorted([self.atoms[p1].id, self.atoms[p2].id])
            key = '{}-{}'.format(first,second)
            force_container = self.bonds.get(key, ForceContainer())
            force_container.append(to_add)

            self.bonds[key] = force_container

    def _parse_harmonic_angles(self, force):
        """ For every set of parameters within the HarmonicAngleForce,
        create an associate HarmonicAngleOmmperator"""
        for i in range(force.getNumAngles()):
            p1, p2, p3, angle, k = force.getAngleParameters(i)
            to_add = HarmonicAngleForceOmmperator(self, force, i)
            first, third = sorted([self.atoms[p1].id, self.atoms[p3].id])
            second = self.atoms[p2].id
            key = '{}-{}-{}'.format(first, second, third)
            force_container = self.angles.get(key, ForceContainer())
            force_container.append(to_add)

            self.angles[key] = force_container

    def _parse_periodic_torsions(self, force):
        """ For every set of parameters within the PeriodicTorsionForce,
        create an associate PeriodicTorsionForceOmmperator """
        for i in range(force.getNumTorsions()):
            p1, p2, p3, p4, n, phase, k = force.getTorsionParameters(i)
            to_add = PeriodicTorsionForceOmmperator(self, force, i)
            p1_id = self.atoms[p1].id
            p2_id = self.atoms[p2].id
            p3_id = self.atoms[p3].id
            p4_id = self.atoms[p4].id
            if p1_id < p4_id:
                key = '{}-{}-{}-{}'.format(p1_id, p2_id, p3_id, p4_id)
            else:
                p1, p2, p3, p4 = p4, p3, p2, p1
                p1_id = self.atoms[p1].id
                p2_id = self.atoms[p2].id
                p3_id = self.atoms[p3].id
                p4_id = self.atoms[p4].id
                key = '{}-{}-{}-{}'.format(p1_id, p2_id, p3_id, p4_id)

            force_container = self.dihedrals.get(key, ForceContainer())
            force_container.append(to_add)

            self.dihedrals[key] = force_container

    def _parse_RB_torsions(self, force):
        """ For every set of parameters within the RBTorsionForce,
        create an associate RBTorsionForceOmmperator """
        for i in range(force.getNumTorsions()):
            p1, p2, p3, p4, c0, c1, c2, c3, c4, c5  = force.getTorsionParameters(i)
            to_add = RBTorsionForceOmmperator(self, force, i)
            p1_id = self.atoms[p1].id
            p2_id = self.atoms[p2].id
            p3_id = self.atoms[p3].id
            p4_id = self.atoms[p4].id
            if p1_id < p4_id:
                key = '{}-{}-{}-{}'.format(p1_id, p2_id, p3_id, p4_id)
            else:
                p1, p2, p3, p4 = p4, p3, p2, p1
                p1_id = self.atoms[p1].id
                p2_id = self.atoms[p2].id
                p3_id = self.atoms[p3].id
                p4_id = self.atoms[p4].id
                key = '{}-{}-{}-{}'.format(p1_id, p2_id, p3_id, p4_id)

            force_container = self.dihedrals.get(key, ForceContainer())
            force_container.append(to_add)

            self.dihedrals[key] = force_container

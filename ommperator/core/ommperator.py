import simtk.openmm as openmm
from .atom import AtomOmmperator
from .bond import HarmonicBondForceOmmperator
from .angle import HarmonicAngleForceOmmperator
from .dihedral import PeriodicTorsionForceOmmperator, RBTorsionForceOmmperator
from .nonbond import NonbondedForceOmmperator, CustomNonbondedForceOmmperator
from .forcecontainer import ForceContainer, CustomForceContainer

class Ommperator:
    """ An interface to operate on openmm systems and topologies 
       
    Parameters
    ---------
    atoms : list of AtomOmmperators
    bonds : list of BondOmmperators
    angles : list of AngleOmmperators
    dihedrals : list of TorsionOmmperators
    nonbonds : list of NonbondOmmperators
    bond_types : dict
        Relates key to ForceContainer of associated BondOmmperators
    angle_types : dict
        Relates key to ForceContainer of associated AngleOmmperators
    dihedral_types : dict
        Relates key to ForceContainer of associated TorsionOmmperators
    nonbond_types : dict
        Relates key to ForceContainer of associated NonbondOmmperators
    """
    def __init__(self, system, topology):
        self.system = system
        self.topology = topology

        self.atoms = []
        self.bonds = [] 
        self.angles = []
        self.dihedrals = []
        self.nonbonds = [] 
        self.custom_nonbonds = [] 

        self.bond_types = {}
        self.angle_types = {}
        self.dihedral_types = {}
        self.nonbond_types = {}
        self.custom_nonbond_types = {}

        self._parse_atoms(topology)

        for force in self.system.getForces():
            if isinstance(force, openmm.HarmonicBondForce):
                self._parse_harmonic_bonds(force)
            if isinstance(force, openmm.HarmonicAngleForce):
                self._parse_harmonic_angles(force)
            if isinstance(force, openmm.PeriodicTorsionForce):
                self._parse_periodic_torsions(force)
            if isinstance(force, openmm.RBTorsionForce):
                self._parse_RB_torsions(force)
            if isinstance(force, openmm.NonbondedForce):
                self._parse_nonbondeds(force)
            if isinstance(force, openmm.CustomNonbondedForce):
                self._parse_custom_nonbondeds(force)


    def _parse_atoms(self, topology):
        self.atoms = [AtomOmmperator(self, atom) for atom in topology.atoms()]

    def _parse_harmonic_bonds(self, force):
        """ For every set of parameters within the HarmonicBondForce,
        create an associated HarmonicBondOmmperator """
        for i in range(force.getNumBonds()):
            p1, p2, length, k = force.getBondParameters(i)
            to_add = HarmonicBondForceOmmperator(self, force, i)
            first, second = sorted([self.atoms[p1].id, self.atoms[p2].id])
            key = '{}-{}'.format(first,second)
            force_container = self.bond_types.get(key, ForceContainer())
            force_container.append(to_add)

            self.bond_types[key] = force_container
            self.bonds.append(to_add)

    def _parse_harmonic_angles(self, force):
        """ For every set of parameters within the HarmonicAngleForce,
        create an associate HarmonicAngleOmmperator"""
        for i in range(force.getNumAngles()):
            p1, p2, p3, angle, k = force.getAngleParameters(i)
            to_add = HarmonicAngleForceOmmperator(self, force, i)
            first, third = sorted([self.atoms[p1].id, self.atoms[p3].id])
            second = self.atoms[p2].id
            key = '{}-{}-{}'.format(first, second, third)
            force_container = self.angle_types.get(key, ForceContainer())
            force_container.append(to_add)

            self.angle_types[key] = force_container
            self.angles.append(to_add)

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

            force_container = self.dihedral_types.get(key, ForceContainer())
            force_container.append(to_add)

            self.dihedral_types[key] = force_container
            self.dihedrals.append(to_add)

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

            force_container = self.dihedral_types.get(key, ForceContainer())
            force_container.append(to_add)

            self.dihedral_types[key] = force_container
            self.dihedrals.append(to_add)


    def _parse_nonbondeds(self, force):
        """ For every set of parameters within the NonbondedForce,
        create an associate NonbondedForceOmmperator """
        for i in range(force.getNumParticles()):
            charge, sigma, epsilon = force.getParticleParameters(i)
            to_add = NonbondedForceOmmperator(self, force, i)
            key = self.atoms[i].id

            force_container = self.nonbond_types.get(key, ForceContainer())
            force_container.append(to_add)

            self.nonbond_types[key] = force_container
            self.nonbonds.append(to_add)

    def _parse_custom_nonbondeds(self, force):
        """ For every set of parameters within the CustomNonbondedForce,
        create an associate CustomNonbonddForceOmmperator """
        for i in range(force.getNumParticles()):
            params = force.getParticleParameters(i)
            to_add = CustomNonbondedForceOmmperator(self, force, i)
            key = self.atoms[i].id

            force_container = self.custom_nonbond_types.get(key, 
                    CustomForceContainer())
            force_container.append(to_add)

            self.custom_nonbond_types[key] = force_container
            self.custom_nonbonds.append(to_add)

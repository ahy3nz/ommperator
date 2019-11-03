# ommperator
Python interface to operate on OpenMM objects

Wrapper around OpenMM system, topology, and force objects.
Mainly used for the force-wrappers (ForceOmmperators) to
modify parameters in groups.
Most Ommperator functions are aimed at operating on or viewing
into the underlying OpenMM system and topology. 
Thus, any functions to modify an Ommperator propagate to the
associated OpenMM object, which is then reflected in other
Ommperator objects.

Example: modify foyer to return an openmm system and topology prior to 
converting into a parmed structure
```python3
import mbuild as mb
import parmed as pmd
from foyer import Forcefield
from mbuild.examples import Ethane
import ommperator
import simtk.unit as unit
import simtk.openmm as openmm
import commpare
import warnings
warnings.simplefilter("ignore")

compound = Ethane()
temp_struc = compound.to_parmed()
ff = Forcefield(name='oplsaa')
system, topology = ff.apply(compound)

my_omm = ommperator.Ommperator(system, topology)

print("Just ethane-oplsaa, no modifications...")
structure = pmd.openmm.load_topology(system=system, topology=topology)
structure.positions = temp_struc.positions
energies = commpare.spawn_engine_simulations(structure, engines=['openmm'])
print(energies)


print("Bond k = 10000, Angle k = 5000...")
for key in my_omm.bonds:
    my_omm.bonds[key].update(k=10000)
for key in my_omm.angles:
    my_omm.angles[key].update(k=5000)
structure = pmd.openmm.load_topology(system=system, topology=topology)
structure.positions = temp_struc.positions
energies = commpare.spawn_engine_simulations(structure, engines=['openmm'])
print(energies)

print("Bond k = 20000, Angle k = 10000...")
for key in my_omm.bonds:
    my_omm.bonds[key].update(k=20000)
for key in my_omm.angles:
    my_omm.angles[key].update(k=10000)
structure = pmd.openmm.load_topology(system=system, topology=topology)
structure.positions = temp_struc.positions
energies = commpare.spawn_engine_simulations(structure, engines=['openmm'])
print(energies)

print("Bond k = 40000, Angle k = 20000...")
for key in my_omm.bonds:
    my_omm.bonds[key].update(k=40000)
for key in my_omm.angles:
    my_omm.angles[key].update(k=20000)

structure = pmd.openmm.load_topology(system=system, topology=topology)
structure.positions = temp_struc.positions
energies = commpare.spawn_engine_simulations(structure, engines=['openmm'])
print(energies)
```


```
Just ethane-oplsaa, no modifications...
             bond       angle  dihedral    nonbond         all
openmm  21.985865  114.052719  0.645149  20.330667  157.014404
Bond k = 10000, Angle k = 5000...
            bond        angle  dihedral    nonbond          all
openmm  0.948956  1818.825317  0.645149  20.330667  1840.750122
Bond k = 20000, Angle k = 10000...
            bond        angle  dihedral    nonbond          all
openmm  1.897911  3637.650635  0.645149  20.330667  3660.524414
Bond k = 40000, Angle k = 20000...
            bond       angle  dihedral    nonbond          all
openmm  3.795823  7275.30127  0.645149  20.330667  7300.072754
```

# NOTE: This script can be modified for different atomic structures, 
# units, etc. See in.elastic for more info.
#

# Define the finite deformation size. Try several values of this
# variable to verify that results do not depend on it.
variable up equal 1.0e-6
 
# Define the amount of random jiggle for atoms
# This prevents atoms from staying on saddle points
variable atomjiggle equal 1.0e-5

# Uncomment one of these blocks, depending on what units
# you are using in LAMMPS and for output

# metal units, elastic constants in eV/A^3
#units		metal
#variable cfac equal 6.2414e-7
#variable cunits string eV/A^3

# metal units, elastic constants in GPa
units		metal
variable cfac equal 1.0e-4
variable cunits string GPa

# real units, elastic constants in GPa
#units		real
#variable cfac equal 1.01325e-4
#variable cunits string GPa

# Define minimization parameters
variable etol equal 0.0 
variable ftol equal 1.0e-10
variable maxiter equal 100
variable maxeval equal 1000
variable dmax equal 1.0e-2

# generate the box and atom positions using a diamond lattice
variable a equal 3.12   # W80_Re20的晶格常数3.12

boundary	p p p

lattice         bcc $a
region		box prism 0 20.0 0 20.0 0 20.0 0.0 0.0 0.0
create_box	2 box

create_atoms	1 box

# Need to set mass to something, just to satisfy LAMMPS
mass  1  183.84		#W BCC  3.14
mass  2  186.2069	#Re  HCP  2.761 

set		type  1   type/ratio  2  0.2  1122  #算出来W80-Re20的晶格常数3.12

write_data Model_WRe.data
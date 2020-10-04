# 3d Lennard-Jones gas

# This block describes general features of the simulation:
#------------------------------------------------------------------------------
units lj # This command selects Lennard-Jones units, meaning that that lengths are measured in units of sigma, energies 
         # in units of epsilon, time in units of tau
dimension 3 # command specifies the dimensionality of the simulation: 2 or 3. Here we run a 3d simulation.
boundary p p p # command specifies boundary conditions to be applied. Here we have periodic boundaries in the x-, y-, 
               # and z- directions.
atom_style atomic # command specifies the complexity of the description of each atom/particle. Here, we will use the 
                  # simplest description, atomic, which is used for noble gases and coarse-grained simulation models.
#------------------------------------------------------------------------------

# This block sets up the dimensions of the 10 ◊ 10 ◊ 10 simulation box and fills the box with atoms with a given 
# packing fraction.
#-----------------------------------------------------------------------------
lattice fcc 0.01 # Command generates a lattice of points. This does, surprisingly enough, not actually generate any 
                 # atoms, it only generates a set of positions in space where atoms will be generated when
                 # we generate atoms. The type fcc specifies a three-dimensional lattice of face-centered-cubic shape.
region simbox block 0 10 0 10 0 10 # command defines a region which is a block extending over 0 < x < 10, 0 < y < 10, 
                                   # 0 < z < 10 We give this region the name simbox.
create_box 1 simbox # Command now actually creates the simulation box based on the spatial region we called simbox. 
                    # The simulation box will only contain 1 (one) type of atoms, hence the number 1.
create_atoms 1 box # Finally fills the simulation box we have defined using the lattice we have defined with atoms of 
                   # type 1.
#-----------------------------------------------------------------------------

# This block defines the material properties of the atoms and defines their initial velocities.
#-----------------------------------------------------------------------------
mass 1 1.0 # atoms of type 1 will have a mass of 1.0
velocity all create 10 711 dist gaussian # initial temperature for all atom 
                                         # types in the system is 10, 711 is the seed
#-----------------------------------------------------------------------------

# This block specifies the potential between the atoms.
#-----------------------------------------------------------------------------
pair_style lj/cut 3.0 # Specifing that we want to use a Lennard-Jones potential 
                      # with a cut-off that is of length 3.0.
pair_coeff 1 1 1.0 1.0 3.0 # The two first numbers, 1 1, specifies that we
                           # describe the interaction of atoms of type 1 with
                           # atoms of type 1.
#-----------------------------------------------------------------------------

fix 1 all nve # all atoms of type 1 have constant; number, volume, energy

# This block specifies simulation control, inclusing output and the number of time-steps to simulate.
#-----------------------------------------------------------------------------
dump 1 all custom 10 dump.lammpstrj id type x y z vx vy vz # command tells the simulator to output the state. The 1 is the 
                                                           # name we give this dump — it could also have been given a
                                                           # name such as mydump. We specify that all atoms are to be output
                                                           # using a custom output format, with output every 10 time-steps
                                                           # to the file dump.lammpstrj, and the ‘id type x y z vx vy vz’ 
                                                           # list specifies what is output per atom.
thermo 100 # command specifies that output to the Terminal and to the log file, log.lammps, is provided every 100 timesteps.
run 5000 # command starts the simulation and specifies that it will run for 5000 timesteps.
#-----------------------------------------------------------------------------
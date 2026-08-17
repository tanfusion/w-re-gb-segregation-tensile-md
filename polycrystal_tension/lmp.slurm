#!/bin/bash
#SBATCH -J lammps
#SBATCH -N 1
#SBATCH --ntasks-per-node=64
#SBATCH -p xahcnormal

module purge
module load lammps/24Dec20-intelmpi-2017
module list
export I_MPI_PMI_LIBRARY=/opt/gridview/slurm/lib/libpmi.so
srun --mpi=pmix lmp_intel_cpu_intelmpi  -i  in.Segregation-tensile.txt  #upper.in为算例名称，自行修改

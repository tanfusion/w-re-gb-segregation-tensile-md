# W-Re Grain-Boundary Segregation and Tensile MD Data

This repository contains the main LAMMPS/ATOMSK scripts and selected data files used in:

> F. Tan, Q. Zhao, T. Qiu, "Synergistic enhancement of strength and ductility in nanocrystalline W-Re alloys via grain boundary sliding and Re segregation: A molecular dynamics study" (manuscript under review).

## Contents

- `potential/` - EAM potential for W-Re (Bonny et al., J. Appl. Phys. 121, 165107, 2017).
- `elastic_constants/` - LAMMPS elastic-constant script, include files, and `compliance.py` parser.
- `lattice_cohesive_energy/` - lattice constant and cohesive energy calculation script and data.
- `gb_segregation_energy/` - Sigma5(210)[001] grain-boundary Re segregation energy script.
- `single_crystal_tension/` - single-crystal W tension script and output.
- `polycrystal_modeling/` - ATOMSK commands, Voronoi seed files, and grain-size distributions for the 200 x 200 x 200 Angstrom nanocrystalline models.
- `polycrystal_tension/` - no-segregation tension (`in.tensile.txt`) and Re MC/MD segregation plus tension (`in.Segregation-tensile.txt`) scripts, with a representative output.
- `temperature_dependence/` - tensile input used for the temperature-dependent runs.
- `bicrystal/` - bicrystal shear/tension scripts, GB segregation modeling script, initial noSeg/Seg models, and example stress-strain output.
- `fracture_energy/` - GB fracture energy script.

## Requirements

- LAMMPS (tested with LAMMPS 24Dec20; scripts use `fix atom/swap`, `fix deform`, `compute stress/atom`, and standard EAM support).
- ATOMSK for polycrystal construction.
- Python 3 with numpy and matplotlib for `lattice_cohesive_energy/cohesive_energy_python.py`.
- OVITO (optional) for visualization and dislocation analysis.

## Workflow

1. Build the single-crystal W reference and the nanocrystalline W models with ATOMSK using the commands in `polycrystal_modeling/modeling_commands.txt` and the seed files in `polycrystal_modeling/seeds/`.
2. Convert a W model to W-20Re, drive Re segregation with hybrid MD/MC, and then apply uniaxial tension:
   `lmp -in in.Segregation-tensile.txt`
3. For the no-segregation reference:
   `lmp -in in.tensile.txt`
4. Bicrystal shear and tension runs use `bicrystal/in.shear.txt` and `bicrystal/in.tensile.txt` together with the provided `WRe_SGMC_Model_noSeg.data` / `WRe_SGMC_Model_Seg.data` models.
5. The GB fracture energy is obtained from `fracture_energy/in.crack_energy.txt`.

## Notes

- Large trajectory dumps are not included. Representative outputs are provided under `example_output/`.
- Slurm scripts are examples from the cluster used for this work; adjust modules, partitions, and MPI settings for your own environment.
- Some original scripts contained Chinese comments; they have been converted to UTF-8 in this repository.
- The EAM potential file is included for reproducibility and should be cited to its original publication:
  G. Bonny, A. Bakaev, D. Terentyev, Y. A. Mastrikov, "Interatomic potential to study plastic deformation in tungsten-rhenium alloys," J. Appl. Phys. 121 (2017) 165107.

## License

Code and data in this repository are provided under the Creative Commons Attribution 4.0 International License.

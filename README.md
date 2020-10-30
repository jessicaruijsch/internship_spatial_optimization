# study_project
 
This folder contains the scripts for the spatial functions of the optimalization.

- calculate_objectives.py --> contains functions to calculate the objective functions
- compute_genome.py --> contains helper functions from CoMOLA to compute patches and genome from the land use map
- initial_population --> contains function to make the initial land use maps and create (called in spatial_sampling.py)
- read_data.py --> reclassification, cropping and reading of input data
- run_nsga2_nonspatial.py --> an example of a non-spatial optimization problem
- run_nsga2_spatial.py --> contains set up of the spatial ngsa2 algorithm and runs the spatial pymoo library
- spatial_crossover.py --> constains spatial crossover functions
- spatial_extention_pymoo.py --> spatial extensions that update the pymoo library
- spatial_mutation.py --> contains spatial mutation functions
- spatial_sampling.py --> creates the initial population

- translate.sh --> takes input maps and translates them to the same resolution and coordinate system using GDAL

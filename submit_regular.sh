#!/bin/bash

# Nombre del trabajo
#SBATCH --job-name=regular-ghostly-sounds
#SBATCH --output=salida.txt
# Cola de trabajo
#SBATCH --partition=full
# Reporte por correo
#SBATCH --mail-type=ALL
#SBATCH --mail-user=egutierreo@uc.cl
# Solicitud de cpus
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

python main_regular_version.py
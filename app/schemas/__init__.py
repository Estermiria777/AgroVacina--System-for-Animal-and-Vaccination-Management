# app/schemas/__init__.py

# 1. Primeiro o vaccine (que não depende de ninguém)
from .vaccine import VaccineCreate, VaccineResponse, VaccineUpdate

# 2. Depois o animal (que depende apenas de vaccine)
from .animal import AnimalBase, AnimalCreate, AnimalResponse, AnimalUpdate

# 3. Por último o owner (que depende de animal)
from .owner import OwnerBase, OwnerCreate, OwnerResponse, OwnerUpdate
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="datascience"

# generic folder structure
list_of_files=[
    ".gthub/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # for ETL pipeline
    f"src/{project_name}/utils/__init__.py",  # for generic functionality
    f"src/{project_name}/utils/common.py", #  for common functionality
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # Training/Testing pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py", # config details
    f"src/{project_name}/constants/__init__.py", # for constant variable
    "config/config.yaml",
    "params.yaml", # hyperparam tuning
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py", # helps create entire proj as package e.g pypi
    "research/research.ipynb", # for doing specific experiments in jupytr
    "templates/index.html", # for flask
    "app.py"

]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:

            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
            


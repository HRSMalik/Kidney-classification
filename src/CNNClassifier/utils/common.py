import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """ 
read a yaml file and return as ConfigBox object

Args:
    path_to_yaml (str): path to the yaml file
    
Returns:
    ConfigBox: ConfigBox object containing the yaml file data
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except yaml.YAMLError as e:
        raise ValueError("yaml file empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create list of directories 

    Args:
        path_to_directories (list): list of directories to create
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created successfully at: {path}")
            

            
            
            
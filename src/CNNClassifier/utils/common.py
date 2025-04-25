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
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    RAises:
        ValueError: If the YAML file is empty or not found.
    
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
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
            

@ensure_annotations
def save_json(path: str, data: dict):
    """
    Save data to json file

    Args:
        path (str): path to save the json file
        data (dict): data to save
    """
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"JSON file saved successfully at: {path}")          
            

@ensure_annotations
def load_json(path: str) -> dict:
    """
    Load data from json file

    Args:
        path (str): path to the json file

    Returns:
        dict: data loaded from the json file
    """
    
    with open(path) as f:
        data = json.load(f)
        logger.info(f"JSON file loaded successfully at: {path}")
        return ConfigBox(data)
    
    
    
@ensure_annotations
def save_bin(path: str, data: Any):
    """
    Save data to binary file

    Args:
        path (str): path to save the binary file
        data (Any): data to save
    """
    
    with open(path, 'wb') as f:
        joblib.dump(data, f)
        logger.info(f"Binary file saved successfully at: {path}")
        

@ensure_annotations
def load_bin(path: str) -> Any:
    """
    Load data from binary file

    Args:
        path (str): path to the binary file

    Returns:
        Any: data loaded from the binary file
    """
    
    with open(path, 'rb') as f:
        data = joblib.load(f)
        logger.info(f"Binary file loaded successfully at: {path}")
        return data
    
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory

    Args:
        path (Path): path to the file or directory

    Returns:
        str: size of the file or directory
    """
    
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"


def decodeImage(imagestring, fileName):
    imgdata = base64.b64decode(imagestring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
    logger.info(f"Image file saved successfully at: {fileName}")
    return fileName


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as imageFile:
        encodedString = base64.b64encode(imageFile.read())
        return encodedString
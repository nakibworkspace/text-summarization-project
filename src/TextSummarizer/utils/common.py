import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotation
from box import Configbox
from pathlib import Path
from typing import Any


@ensure_annotation
def read_yaml(path_to_yaml: Path) -> Configbox:
    '''reads the yaml file and returns 
    
    Args:
        path_to_yaml(str): path to input
    Raises:
        ValueError: if yaml file is empty
        e: empty File 
    Returns:
        Configbox: loaded configbox'''
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return Configbox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotation
def create_directories(path_to_directories: list, verbos=True):
    '''create list of directories
    Args: 
    path_to_directories(list): list of directory paths
    ignore_log(bool, optional): ignore if multiple directories is to be directed
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbos:
            logger.info(f"Directory {path} created successfully")
            
@ensure_annotation
def get_size(path: Path) -> str:
    '''get size in KB
    Args: 
    path(Path): path to file
    returns:
    size in kb'''
    size_in_kb= round(os.path.getsize(path)/1024)
    return f" {size_in_kb} KB"
    
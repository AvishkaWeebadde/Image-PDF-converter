"""
Utility functions for the image-PDF converter
"""

import os
from pathlib import Path
from typing import List, Union
from converter.exceptions import FileNotFoundError, PermissionError

"""
    Validate that a file exists and is readable
    
    Args:
        file_path: Path to file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If file is not readable
"""
def validate_file_exists(file_path: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Path is not a file: {file_path}")
    
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"File is not readable: {file_path}")
    

"""
    Create directory if it doesn't exist
    
    Args:
        dir_path: Directory path
        
    Raises:
        PermissionError: If directory cannot be created
"""
def create_directory(dir_path: Union[str, Path]) -> None:
    try:
        os.makedirs(dir_path, exist_ok=True)
    except OSError as e:
        raise PermissionError(f"Cannot create directory {dir_path}: {e}")
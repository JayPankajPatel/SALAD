"""
File I/O for creating and storing pictures.

This module provides functions to create directories for storing pictures.
"""

import os


def create_directory(directory_path: str) -> None:
    """
    Create a directory at the specified path.

    :param arg1: directory_path: The path of the directory to create.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as exp:
        print(f"Error creating directory: {directory_path}\n{exp}")


def create_directory_in_script_location(directory_name: str) -> None:
    """
    Create a directory in the location of the script.

    :param arg1: directory_name: The name of the directory to create.
    """
    script_location = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(script_location, directory_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


# Example usage
if __name__ == "__main__":
    directory_name = "pictures"
    create_directory_in_script_location(directory_name)

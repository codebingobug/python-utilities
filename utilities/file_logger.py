# -*- coding: utf-8 -*-
"""
This module contains a utility function for creating a logger with a file handler.
    - The main function in this module is `get_logger_with_file`,
        which creates a logger with a file handler.
"""

import logging


def get_logger_with_file(name=None):
    """
    This function returns a logger equipped with a file handler.
    Initially, it verifies if the logger has already been modified, 
    if not, it appends a stream handler with INFO level.
    Subsequently, it generates a file handler with DEBUG level.

    Parameters:
    name (str): The designated name of the logger. If no name is given, 'root' is utilized.
    
    Returns:
    logger (Logger): The logger furnished with a file handler.
    """
    # Initialize a logger with the provided name.
    logger = logging.getLogger(name)
    flag_name = name if name else 'root'
    # If the logger already has Filter with name 'MediaTest', return the configured logger directly.
    if any(f.name == flag_name for f in logger.filters):
        return logger

    logger.addFilter(logging.Filter(flag_name))

    # Configure logger.
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Add a stream handler to the logger.
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Create a file handler with the logger's name or "debug" if no name is provided.
    log_file_name = f'{name}.log'
    file_handler = logging.FileHandler(log_file_name, "w")
    # Check if a file handler with the same filename already exists.
    duplicate_handler = any(
        isinstance(
            handler, logging.FileHandler) and handler.baseFilename == file_handler.baseFilename
        for handler in logger.handlers)
    # If no duplicate handler exists, add the new file handler to the logger.
    if not duplicate_handler:
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info("logger['%s'].FileHandler('%s') added.", name, log_file_name)
    # The function returns the logger.
    return logger

import os
import logging
import unittest
from utilities.file_logger import get_logger_with_file


class TestFileLogger(unittest.TestCase):
    def test_get_logger_with_file(self):
        # Create a logger with the name 'test'
        logger = get_logger_with_file('test')

        # Check that the logger has the correct name
        self.assertEqual(logger.name, 'test', 'Logger name not set correctly')

        # Check that the logger has a StreamHandler
        self.assertTrue(any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers),
                        'StreamHandler not added to logger')

        # Check that the logger has a FileHandler
        self.assertTrue(any(isinstance(handler, logging.FileHandler) for handler in logger.handlers),
                        'FileHandler not added to logger')

        # Check that the log file was created
        self.assertTrue(os.path.exists('test.log'), 'Log file not created')

        # Write a log message
        logger.info('Test message')

        # Check that the log message was written to the file
        with open('test.log', 'r') as f:
            log_content = f.read()
        self.assertIn('Test message', log_content, 'Log message not written to file')

        # Clean up the log file
        os.remove('test.log')

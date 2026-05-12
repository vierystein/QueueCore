# test_queuecore.py
"""
Tests for QueueCore module.
"""

import unittest
from queuecore import QueueCore

class TestQueueCore(unittest.TestCase):
    """Test cases for QueueCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QueueCore()
        self.assertIsInstance(instance, QueueCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QueueCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_optisync.py
"""
Tests for OptiSync module.
"""

import unittest
from optisync import OptiSync

class TestOptiSync(unittest.TestCase):
    """Test cases for OptiSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OptiSync()
        self.assertIsInstance(instance, OptiSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OptiSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

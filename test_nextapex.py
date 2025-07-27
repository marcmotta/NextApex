# test_nextapex.py
"""
Tests for NextApex module.
"""

import unittest
from nextapex import NextApex

class TestNextApex(unittest.TestCase):
    """Test cases for NextApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextApex()
        self.assertIsInstance(instance, NextApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

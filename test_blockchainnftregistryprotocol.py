# test_blockchainnftregistryprotocol.py
"""
Tests for BlockchainNFTRegistryProtocol module.
"""

import unittest
from blockchainnftregistryprotocol import BlockchainNFTRegistryProtocol

class TestBlockchainNFTRegistryProtocol(unittest.TestCase):
    """Test cases for BlockchainNFTRegistryProtocol class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTRegistryProtocol()
        self.assertIsInstance(instance, BlockchainNFTRegistryProtocol)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTRegistryProtocol()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

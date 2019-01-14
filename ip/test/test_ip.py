import os
import pdb
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from ip import IP

class Test(unittest.TestCase):
    def test_ip_init(self):
        ip = IP()
        self.assertTrue(ip.init_address("10.0.0.1/24"))

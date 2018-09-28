import os
import pdb
import sys

sys.path.insert(0, "..")

from src.ip import IP


ip = IP()
ip.init_address("10.0.0.1/24")
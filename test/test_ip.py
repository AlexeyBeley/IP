import os
import pdb
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from ip import IP


class Test(unittest.TestCase):
    def test_ip_init(self):
        ip = IP("10.0.0.1/24")
        self.assertTrue(isinstance(ip, IP))

    def test_convert_short_to_long_ipv6(self):
        assert IP.convert_short_to_long_lst_ipv6("::") == ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
        assert IP.convert_short_to_long_lst_ipv6("::1100") == ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "1100"]
        assert IP.convert_short_to_long_lst_ipv6("0::1") == ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0001"]
        assert IP.convert_short_to_long_lst_ipv6("1:10::1") == ["0001", "0010", "0000", "0000", "0000", "0000", "0000", "0001"]
        assert IP.convert_short_to_long_lst_ipv6("1:10::10:1") == ["0001", "0010", "0000", "0000", "0000", "0000", "0010", "0001"]
        assert IP.convert_short_to_long_lst_ipv6("1::10:1") == ["0001", "0000", "0000", "0000", "0000", "0000", "0010", "0001"]
        assert IP.convert_short_to_long_lst_ipv6("1:1:1:1:1:1:1:1") == ["0001", "0001", "0001", "0001", "0001", "0001", "0001", "0001"]
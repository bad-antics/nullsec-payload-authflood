import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_payload_authflood.core import AuthFloodDetector

class TestFlood(unittest.TestCase):
    def test_no_flood(self):
        d=AuthFloodDetector(threshold=50)
        d.log_auth("AA:BB:CC:DD:EE:FF")
        self.assertFalse(d.detect_flood()["flooding"])
    def test_flood(self):
        d=AuthFloodDetector(threshold=5)
        for i in range(10): d.log_auth(f"AA:BB:CC:DD:EE:{i:02X}")
        self.assertTrue(d.detect_flood()["flooding"])

if __name__=="__main__": unittest.main()

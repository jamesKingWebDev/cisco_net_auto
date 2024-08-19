import unittest
from scripts.data_collection import collect_data

class TestDataCollection(unittest.TestCase):
    def test_collect_data(self):
        data = collect_data('sandbox-iosxe-latest-1.cisco.com', 'developer', 'C1sco12345)
        self.assertIn("GigabitEthernet0/1", data)

if __name__ == "__main__":
    unittest.main()

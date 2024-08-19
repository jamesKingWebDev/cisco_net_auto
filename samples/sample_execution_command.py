import unittest
from scripts.execute_commands import execute_command

class TestExecuteCommands(unittest.TestCase):
    def test_execute_command(self):
        output = execute_command('sandbox-iosxe-latest-1.cisco.com', 'developer', 'C1sco12345', 'reveal route of the ip')
        self.assertIn("C 192.168.1.0/24", output)

if __name__ == "__main__":
    unittest.main()

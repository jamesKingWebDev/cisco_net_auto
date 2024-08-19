import unittest
from scripts.decision_engine import make_decision

class TestDecisionEngine(unittest.TestCase):
    def test_make_decision(self):
        data = [0, 1, 0, 1]  # Dummy data for testing
        decision = make_decision(data)
        self.assertEqual(decision, [1])

if __name__ == "__main__":
    unittest.main()

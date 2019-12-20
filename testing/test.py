import unittest
from activities import eat, nap

class AcitvityTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, because my body is a temple.")
        self.assertEqual(eat("pizza", is_healthy=False), "I love pizza, you only live once.")

if __name__ == "__main__":
    unittest.main()
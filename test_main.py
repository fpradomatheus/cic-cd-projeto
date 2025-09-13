import unittest
from main import soma

class TestSoma(unittest.TestCase):
    def test_soma_basica(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()

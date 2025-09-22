import unittest
from main import soma, subtracao

class TestOperacoes(unittest.TestCase):

    def test_soma_basica(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_soma_floats(self):
        self.assertAlmostEqual(soma(2.5, 3.1), 5.6, places=7)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_subtracao_basica(self):
        self.assertEqual(subtracao(5, 3), 2)

    def test_subtracao_negativos(self):
        self.assertEqual(subtracao(-1, -1), 0)

    def test_zero(self):
        self.assertEqual(soma(0, 0), 0)

if __name__ == "__main__":
    unittest.main()




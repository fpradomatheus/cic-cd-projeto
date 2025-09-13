import unittest
from main import soma, subtracao

class TestOperações(unittest.TestCase):

    def test_soma_basica(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
    
    def test_subtracao_basica(self):
        self.assertEqual(subtracao(5, 3), 2)

if __name__ == "__main__":
    unittest.main()

#teste correcao
#teste correcao 2


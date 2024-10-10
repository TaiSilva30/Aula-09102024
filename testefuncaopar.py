import unittest

from testepar import eh_par

class TestEhPar(unittest.TestCase):
    def test_eh_par(self):
        self.assertTrue(eh_par(2))

    def test_eh_impar(self):
        self.assertFalse(eh_par(3))

if __name__ == '__main__':
    unittest.main()
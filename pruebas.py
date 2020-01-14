import unittest
import complejos

z1=(1,2)
z2=(2,3)

z1=(0,-3)
z2=(3,-10)

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(complejos.sumacomplex((1,2),(2,3)), (3, 5))
##        self.assertEqual(complejos.sumacomplex((0,-3),(3,-10)), (3, -13))
        
    def test_resta(self):
        self.assertEqual(complejos.restacomplex((1,2),(2,3)), (-1, -1))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (-3, 7))
        
    def test_multi(self):
        self.assertEqual(complejos.multicomplex((1,2),(2,3)), (-4, 7))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (-30, -9))

    def test_div(self):
        self.assertEqual(complejos.divcomplex((1,2),(2,3)), (0.6153846153846154, 0.07692307692307693))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (0.27522935779816515, -0.08256880733944955))

    def test_mod(self):
        self.assertEqual(complejos.modcomplex((1,2)), 2.23606797749979)
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), 3.0)

    def test_conj(self):    
        self.assertEqual(complejos.conjcomplex((1,2)), (1, -2))
        ##self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (0, 3))

    def test_polar(self):
        self.assertEqual(complejos.polarcomplex((1,2)), (2.23606797749979, 1.1071487177940904))
        ##self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), "ERROR Division Por Cero")


if __name__ == '__main__':
    unittest.main()
    

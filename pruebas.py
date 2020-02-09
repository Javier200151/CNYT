import unittest
import LibreriaComplejos

z1=(1,2)
z2=(2,3)

z1=(0,-3)
z2=(3,-10)

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(LibreriaComplejos.sumacomplex((1,2),(2,3)), (3, 5))
##        self.assertEqual(complejos.sumacomplex((0,-3),(3,-10)), (3, -13))
        
    def test_resta(self):
        self.assertEqual(LibreriaComplejos.restacomplex((1,2),(2,3)), (-1, -1))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (-3, 7))
        
    def test_multi(self):
        self.assertEqual(LibreriaComplejos.multicomplex((1,2),(2,3)), (-4, 7))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (-30, -9))

    def test_div(self):
        self.assertEqual(LibreriaComplejos.divcomplex((1,2),(2,3)), (0.6153846153846154, 0.07692307692307693))
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (0.27522935779816515, -0.08256880733944955))

    def test_mod(self):
        self.assertEqual(LibreriaComplejos.modcomplex((1,2)), 2.23606797749979)
##        self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), 3.0)

    def test_conj(self):    
        self.assertEqual(LibreriaComplejos.conjcomplex((1,2)), (1, -2))
        ##self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), (0, 3))

    def test_polar(self):
        self.assertEqual(LibreriaComplejos.polarcomplex((-3,2)), (3.605551275463989, -2.356194490192345))
        ##self.assertEqual(complejos.restacomplex((0,-3),(3,-10)), "ERROR Division Por Cero")

    def test_sumavector(self):
        v1=[(6,-4),(7,3),(4.2,-8),(0,-3)]
        v2=[(16,2),(0,-7),(6,0),(0,-4)]
        self.assertEqual(LibreriaComplejos.sumavector(v1,v2), [(22, -2), (7, -4), (10.2, -8), (0, -7)])

    def test_inversovector(self):
        v1=[(6,-4),(7,3),(4,-8),(0,-3)]
        self.assertEqual(LibreriaComplejos.inversovector(v1), [(-6, 4), (-7, -3), (-4, 8), (0, 3)])

    def test_conjugadavector(self):
        v1=[(16,2),(0,-7),(6,0),(0,-4)]
        self.assertEqual(LibreriaComplejos.conjugadavector(v1), [(16, -2), (0, 7), (6, 0), (0, 4)])

    def test_Vectorsproductotensor(self):
        v1=[(6,-4),(7,3),(4.2,-8),(0,-3)]
        v2=[(16,2),(0,-7),(6,0),(0,-4)]
        self.assertEqual(LibreriaComplejos.Vectorsproductotensor(v1,v2), [(104, -52), (-28, -42), (36, -24), (-16, -24), (106, 62), (21, -49), (42, 18), (12, -28), (83.2, -119.6), (-56.0, -29.4), (25.2, -48.0), (-32.0, -16.8), (6, -48), (-21, 0), (0, -18), (-12, 0)])

    def test_adicionmatrices(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
        self.assertEqual(LibreriaComplejos.adicionmatrices(m1,m2), [[(4, 5), (3, 3)], [(1, 3), (2, 2)]])

    def test_inversamatriz(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        self.assertEqual(LibreriaComplejos.inversamatriz(m1),[[(-3, -2), (-3, -1)], [(0, -2), (-1, -2)]])

    def test_multescalarmatrices(self):
        z1=(0,-3)
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        self.assertEqual(LibreriaComplejos.multescalarmatrices(z1,m1),[[(6, -9), (3, -9)], [(6, 0), (6, -3)]])
 
    def test_matriztranspuesta(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        self.assertEqual(LibreriaComplejos.matriztranspuesta(m1),[[(3, 2), (0, 2)], [(3, 1), (1, 2)]])
 
    def test_conjmatriz(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        self.assertEqual(LibreriaComplejos.conjmatriz(m1),[[(3, -2), (0, -2)], [(3, -1), (1, -2)]])

    def test_adjmatriz(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        self.assertEqual(LibreriaComplejos.adjmatriz(m1),[[(3, -2), (3, -1)], [(0, -2), (1, -2)]])

    def test_innermatrix(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]   
        self.assertEqual(LibreriaComplejos.innermatrix(m1,m2),(-5, 32))
        
    def test_matrizmult(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]   
        self.assertEqual(LibreriaComplejos.matrizmult(m1,m2),[[(-1, 15), (-1, 7)], [(-7, 5), (-3, 2)]])

    def test_matrizdis(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]   
        self.assertEqual(LibreriaComplejos.matrizdis(m1,m2),4.58257569495584)

    def test_isUnitaria(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]   
        self.assertEqual(LibreriaComplejos.isUnitaria(m1),False)
        self.assertEqual(LibreriaComplejos.isUnitaria(m2),False)

    def test_isHermitania(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]   
        self.assertEqual(LibreriaComplejos.isHermitania(m1),False)
        self.assertEqual(LibreriaComplejos.isHermitania(m2),False)

    def test_sumacompvector(self):
        v1=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
        v2=[(16,2.3),(0,-7),(6,0),(0,-4)]  
        self.assertEqual(LibreriaComplejos.sumacompvector(v1),(17.2, -12.1))
        self.assertEqual(LibreriaComplejos.sumacompvector(v2),(22, -8.7))

    def test_norma(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
        self.assertEqual(LibreriaComplejos.norma(m1),5.656854249492381)
        self.assertEqual(LibreriaComplejos.norma(m2),4.123105625617661)

    def test_productotensor(self):
        m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
        m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
        self.assertEqual(LibreriaComplejos.productotensor(m1,m2),[[(-3, 11), (-4, 6), (0, 10), (-2, 6)], [(1, 5), (3, 2), (2, 4), (3, 1)], [(-6, 2), (-4, 0), (-5, 5), (-4, 2)], [(-2, 2), (0, 2), (-1, 3), (1, 2)]])

if __name__ == '__main__':
    unittest.main()

import unittest
from atomOTHER import AtomOTHER

class TestAtomOTHER(unittest.TestCase):

    def setUp(self):
        self._haz = 'abc'
        self._haz2 = 'def'
        self._total = {'haz3':'hij', 'haz4':'klm'}
        self._flaw = [1,2,3]

        self._atomOTHER1 = AtomOTHER()
        self._atomOTHER2 = AtomOTHER(self._total)
        self._atomOTHER3 = AtomOTHER(self._flaw)

    def tearDown(self):
        self._haz = None
        self._haz2 = None
        self._total = None
        self._flaw = None
        self._atomOTHER1 = None
        self._atomOTHER2 = None
        self._atomOTHER3 = None


    def test_get(self):
        self.assertEqual(self._atomOTHER1.Get('useless'), None) #doesnt exist
        
        self.assertEqual(self._atomOTHER2.Get('haz'), None) #doesnt exist
        self.assertEqual(self._atomOTHER2.Get('haz3'), 'hij')
        self.assertEqual(self._atomOTHER2.Get('haz4'), 'klm')

        
    
    def test_set(self):
        
        self._atomOTHER1.Set('haz1', self._haz)
        self._atomOTHER1.Set('haz2', self._haz2)
        self.assertEqual(self._atomOTHER1.Get('haz1'), self._haz)
        self.assertEqual(self._atomOTHER1.Get('haz2'), self._haz2)
        
        self.assertEqual(self._atomOTHER1.Get('useless'), None)

        self._atomOTHER1.Set('haz1', 1)
        self._atomOTHER1.Set('haz2', 2)
        self._atomOTHER1.Set(1, self._haz)
        self.assertEqual(self._atomOTHER1.Get('haz1'), 1)
        self.assertEqual(self._atomOTHER1.Get('haz2'), 2)
        self.assertEqual(self._atomOTHER1.Get(1), self._haz)


    def test_allattr(self):
        self.assertEqual(self._atomOTHER2.AllAttr(), self._total)
        
        self._atomOTHER2.Set(2, '2')
        self.assertEqual(self._atomOTHER2.AllAttr(), {'haz3':'hij', 'haz4':'klm', 2:'2'})

        self.assertEqual(self._atomOTHER3.AllAttr(), {})

    def test_delete(self):
        self._atomOTHER2.Delete(2)
        self.assertEqual(self._atomOTHER2.AllAttr(), {'haz3':'hij', 'haz4':'klm'})
        self.assertEqual(self._atomOTHER2.Get(2), None)

        self._atomOTHER2.Delete('haz5')
        self.assertEqual(self._atomOTHER2.AllAttr(), {'haz3':'hij', 'haz4':'klm'})
        self.assertEqual(self._atomOTHER2.Get('haz5'), None)

        self._atomOTHER2.Delete('haz3')
        self.assertEqual(self._atomOTHER2.AllAttr(), {'haz4':'klm'})
        self.assertEqual(self._atomOTHER2.Get('haz3'), None)



    """def test_str(self):
        aux1 = 'GENERAL\n'
        aux2 = aux1+'haz3:hij\nhaz4:klm\n'
        """



if __name__ == "__main__":
    unittest.main(exit = False)
        
        

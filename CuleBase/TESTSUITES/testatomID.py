import unittest
from atomID import AtomID

class TestAtomID(unittest.TestCase):
    def setUp(self):
        self._name = 'Carbon'
        self._abbr = 'C'
        self._anum = 12
        self._amas = 12.011
        self._econ = ['1s2','2s2','2p2']

        self._atom = AtomID(self._name, self._abbr,
                            self._anum, self._amas,
                            self._econ)

    def tearDown(self):
        self._name = None
        self._abbr = None
        self._anum = None
        self._amas = None
        self._econ = None
        self._atom = None

    def test_get(self):
        self.assertEqual(self._atom.Get('Name'), 'Carbon')
        self.assertEqual(self._atom.Get('Abbreviation'), 'C')
        self.assertEqual(self._atom.Get('Atomic Number'), 12)
        self.assertEqual(self._atom.Get('Atomic Mass'), 12.011)
        self.assertEqual(self._atom.Get('Electron Configuration'),
                                         ['1s2','2s2','2p2'])

        self.assertEqual(type(self._atom.Get('Atomic Mass')),
                          type(float()))

        self.assertEqual(self._atom.Get('useless'), None)


    def test_str(self):
        aux = 'IDENTITY\nName:Carbon\nAbbreviation:C\nAtomic Number:12\nAtomic Mass:12.011\nElectron Configuration:1s2,2s2,2p2\n'

        self.assertEqual(str(self._atom), aux)


if __name__ == '__main__':
    unittest.main(exit=False)
        
        

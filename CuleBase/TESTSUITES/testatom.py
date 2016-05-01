import unittest
from atom import Atom
from atomID import AtomID
from atomOTHER import AtomOTHER

class TestAtom(unittest.TestCase):
    def setUp(self):
        self._C_name = 'Carbon'
        self._C_abbr = 'C'
        self._C_anum = 12
        self._C_amas = 12.011

        self._C_OTHER = {'Hazards':'Causes Life'}

        self._H_name = 'Hydrogen'
        self._H_abbr = 'H'
        self._H_anum = 1
        self._H_amas = 1.01

        self._C_atomID = AtomID(self._C_name, self._C_abbr,
                                self._C_anum, self._C_amas)
        self._H_atomID = AtomID(self._H_name, self._H_abbr,
                                self._H_anum, self._H_amas)
        self._C_atomOTHER = AtomOTHER(self._C_OTHER)

        self._C = Atom(self._C_atomID, self._C_atomOTHER)
        self._H = Atom(self._H_atomID)


    def tearDown(self):
        self._C_name = None
        self._C_abbr = None
        self._C_anum = None
        self._C_amas = None

        self._C_OTHER = None

        self._H_name = None
        self._H_abbr = None
        self._H_anum = None
        self._H_amas = None

        self._C_atomID = None
        self._H_atomID = None
        self._C_atomOTHER = None

        self._C = None
        self._H = None


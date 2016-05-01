class AtomID(object):

    def __init__(self, name:str, abbr:str, atomic_number:int, atomic_mass:float)->None:
        self._attr = {'Name': name,
                      'Abbreviation': abbr,
                      'Atomic Number': atomic_number,
                      'Atomic Mass': atomic_mass}


    def Get(self, attr:str):
        """returns the value of the attribute in the dictionary of attributes"""
        try:
            return self._attr[attr]
        except (KeyError):
            return None #may need modification in future

    def __str__(self):
        aux = 'IDENTITY\nName:{}\nAbbreviation:{}\nAtomic Number:{}\nAtomic Mass:{}\n'.format(
            self._attr['Name'], self._attr['Abbreviation'], self._attr['Atomic Number'], self._attr['Atomic Mass'])
        return aux
    

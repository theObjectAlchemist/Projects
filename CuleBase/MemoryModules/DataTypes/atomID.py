class AtomID(object):

    def __init__(self, name:str, abbr:str, atomic_number:int, atomic_mass:float, e_config:list)->None:
        self._attr = {'Name': name,
                      'Abbreviation': abbr,
                      'Atomic Number': atomic_number,
                      'Atomic Mass': atomic_mass,
                      'Electron Configuration': e_config}


    def Get(self, attr:str):
        """returns the value of the attribute in the dictionary of attributes"""
        try:
            return self._attr[attr]
        except (KeyError):
            return None #may need modification in future

    def __str__(self):
        e_config = ''
        for i in range(0,len(self._attr['Electron Configuration'])):
            e_config += self._attr['Electron Configuration'][i]
            if i < len(self._attr['Electron Configuration'])-1:
                e_config += ','
        aux = 'IDENTITY\nName:{}\nAbbreviation:{}\nAtomic Number:{}\nAtomic Mass:{}\nElectron Configuration:{}\n'.format(
            self._attr['Name'], self._attr['Abbreviation'], self._attr['Atomic Number'], self._attr['Atomic Mass'],
            e_config)
        return aux
    

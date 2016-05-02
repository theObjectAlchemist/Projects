class AtomOTHER(object):

    def __init__(self, attr = {}):
        if type(attr) != type(dict()):
            attr = {}
        self._attr = attr
        

    def Set(self, attr:str, value)->None:
        """sets a value for the specified attribute. creates if new, overwrites if exists"""
        self._attr[attr] = value

    def Get(self, attr:str)->object:
        """gets the value at the specified attribute, None if doesnt exist"""
        try:
            return self._attr[attr]
        except (KeyError):
            return None #may need modification

    def Delete(self, attr:str)->None:
        """Deletes the attribute and its associated value"""
        try:
            aux = self._attr.pop(attr)
        except (KeyError):
            return None

    def AllAttr(self)->dict:
        """returns a dictionary type of all attributes"""
        return self._attr

    def IsEmpty(self)->bool:
        """returns a bool indicating if there are any attributes"""
        if self._attr == {}:
            return True
        return False

    def __str__(self):
        aux = 'GENERAL\n'
        for i in self._attr:
            aux += '{}:{}\n'.format(i, self._attr[i])
        return aux
            

    

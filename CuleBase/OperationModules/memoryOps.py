from atomGenerator import AtomGenerator

import sys
sys.path.insert(0, 'C:/DzasterusTesting/Team/CuleBase/MemoryModules/ReaderWriter/')
from atomwriter import AtomWriter



def prompt(pr=''):#, accept = []):
    return (input("<o> {}".format(pr)))




def CreateNewAtom():

    newAtomGen = AtomGenerator()

    aux = newAtomGen.PromptUserForID()
    newAtomGen.SetAtomID(aux[0],aux[1],
                         aux[2],aux[3])
    #populate with other info here? not too sure
    #thats better suited for "edit" in my opinion
    return newAtomGen.GenerateAtom()




def SaveAtom(elem, path = ''):
    """can only take Atom objects"""
    writerwriter = AtomWriter()
    writerwriter.WriteAtomToFile(elem, path)
    #modify this to specify a path maybe? as an option





def AddToAtomicDataBase(): #================THIS IS A TEMPORARY FUNCTION================#
    sel = prompt()

    while sel != 'end':
        aux = CreateNewAtom()
        SaveAtom(aux, 'C:/DzasterusTesting/Team/CuleBase/DataBase/Atoms/')
        sel = prompt()
    


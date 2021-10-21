'''
                    Bytes Chains
                Manipulation Functions
'''

import struct as s
from typing import Dict, Tuple, Callable, List


def     ushort_uint(byts: bytes) -> Tuple[int, int]:
    '''
    Takes a bytes buffer then extract a 
    short unsigned int & a 32-bits unsigned int b
    both in big-endian (>)
    '''

    results = [None, None]
    results[0] = s.unpack_from('>H', byts, 0)[0]
    results[1] = s.unpack_from('>I', byts, 2)[0]

    return tuple(results)




def     buf2latin(byts: bytes) -> Tuple[int, str]:

    '''
    Takes a bytes buffer then extract an 
    iso latin1 string precessed by its size
    '''
    
    mesured_str = [None, '']
    pos = 2

    #SAVES LENGTH
    mesured_str[0] = s.unpack_from('>H', byts, 0)[0]
    
    
    #EXTRACT STR
    #converts directly byts to latin-1 str
    length = mesured_str[0]
    mesured_str[1] = str(byts[2:length+2], encoding='latin-1')

    
    #iterative extraction
    #in case of
    '''
    while (pos - 1) <= mesured_str[0]:
        c = str(object=(s.unpack_from('1c', byts, pos)[0]), encoding='latin-1')
        #print(type(c)) 
        mesured_str[1] = mesured_str[1] + c#(s.unpack_from('1c', byts, pos)[0])
        pos += 1
    '''
    
    return tuple(mesured_str)


def     ascii2buf(*strs: str) -> bytes:
    '''
    Takes a variable number of strings and transforms
    them in a byters buffer respecting the following:

                   Number of elemets        as 32-bits unsigned int
    then           Concatenated chains      each
    precessed by   Chain length             as 16-bits unsigned int
    '''
    Buffer = b''
    Nb_str = 0
    Len = 0

    #Counts strings and pack that number
    for count in strs:    Nb_str += 1
    Buffer = Buffer + s.pack('>I', Nb_str)

    #Packs Chains and their length
    for chain in strs:
        Len = len(chain)
        Buffer = Buffer + s.pack('>h', Len)
        format = '>'+ str(Len) + 's'
        Buffer = Buffer + s.pack(format, bytes(chain, 'UTF-8'))

    return Buffer
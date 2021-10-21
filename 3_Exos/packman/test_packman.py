import my_packman as pkman

print('TEST 1\n')

assert pkman.ushort_uint(b'\x01\x42\x00\x01\x02\x03\xde\xad') == (322, 66051)



print('\nTEST 2')

assert pkman.buf2latin(b'\x00\x04G\xE9g\xe9zzz') == (4, 'Gégé')



print('\nTEST 3')

assert pkman.ascii2buf("I", "like", "the", "game") == bytearray(b'\x00\x00\x00\x04\x00\x01I\x00\x04like\x00\x03the\x00\x04game')
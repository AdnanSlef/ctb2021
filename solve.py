from binascii import hexlify as hh, unhexlify as uh

outer_rim = '43DC1162DC117D0008721852FB1E3C2AB85FAF0AF930C5B6C1D24FAEDFABB776'
inner_rim = [('00000000000','0000000133E'), ('54DC8BF6C2','D864376430D'), ('376DADECB0A','03EDF99AB7')]

print(len(outer_rim),outer_rim)

inner_str = ''.join(x for y in inner_rim for x in y) 
reference = '000000000000000000067119c310ecee2c2f4b79b96e2a616ff93bf31236e1d6'
print(len(inner_str),inner_str)
print(len(reference),reference)

op_return = uh('68747470733a2f2f746162636f6e662e636f6d2f73636176656e67657268756e74')
print(op_return)

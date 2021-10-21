# -*- coding: utf-8 -*-

# int to bytes

n = 36
n_b = n.to_bytes(8,byteorder='little')
# "$\0 ..."
n1 = int.from_bytes(n_b, byteorder='little',signed=False)
assert n == n1
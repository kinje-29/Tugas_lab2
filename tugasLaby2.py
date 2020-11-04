#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:09:38 2020

@author: fajar
"""

a = eval(input("Masukan nilai a: "))
b = eval(input("masukan Nilai b: "))

print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan{1}&{0}=%d".format(a,b) % (a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print ("hasil pemjumlahan {1}+{0}=%d".format(a,b) % (a+b))
print ("hasil penjumlahan {1}/{0}=%d".format(a,b) % (a/b))
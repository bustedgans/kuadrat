#mau ngapain?recode?malu tolol
#gua buat biar gua pintar asu
from __future__ import print_function
import sys
import os
import math
import time

b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'


print ('\033[31;1m[----------------------------------------------]')
print ('\033[31;1m[               Author : Insan Gans            ]')
print ('\033[31;1m[             Team : ATTACKER NETWORK TEAM     ]')
print ('\033[31;1m[             Contact Me : 081295978029        ]')
print ('\033[31;1m[----------------------------------------------]')
print('')


def main():
   
   print ("\033[35;1mAKAR-AKAR PERSAMAAN KUADRAT")
   print ('')
   a = int(input('\033[32;1mMasukkan nilai \033[37;1m[\033[32;1ma\033[37;1m] : '))
   b = int(input('\033[35;1mMasukkan nilai \033[37;1m[\033[32;1mb\033[37;1m] : '))
   c = int(input('\033[32;1mMasukkan nilai \033[37;1m[\033[32;1mc\033[37;1m] : '))

   
   D = (b*b) - (4*a*c)

   if D < 0:
      print ("\033[31;1makar-akar imajiner, exitting...")
      sys.exit(1)

   elif D == 0:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x1 = x2

   else:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = (-b - math.sqrt(D)) / (2*a) 

   
   print ("\nx1 = %d" %x1)
   print ("x2 = %d" %x2)

if __name__ == "__main__":

    main()
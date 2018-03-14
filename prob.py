from decimal import *

getcontext().prec = 100

base = Decimal(1)
for i in range(100):
  base *= Decimal(1/24)

print(base)

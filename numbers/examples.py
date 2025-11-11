# integers - basics
10

10 + 2  # 12  (int)
10 * 2  # 20  (int)
10 / 2  # 5.0 (float)

10 // 2  # 5

0.5 * 10  # 5.0
0.0 == 0

10**6  # to the power of 6

# big numbers
1_000
10_000_000

# floats
0.0
.5

# calculations
0.1 + 0.2  # 0.30000000000000004

# Decimals
from decimal import Decimal

Decimal(1) == Decimal(1.0) == Decimal("1")  # True

Decimal(0) == Decimal()

Decimal(1.5) == Decimal("1.5")  # True

Decimal(0.2) == Decimal("0.2")  # ?
Decimal(0.2)  # Decimal('0.200000000000000011102230246251565404236316680908203125')

# Safe
Decimal(str(0.2))
Decimal("0.2")

Decimal(2) * 5  # Decimal('10')

# rounding
round(1.5)  # 2
round(2.5)  # ?
round(3.5)  # 4
round(4.5)  # ?

# Banker's rounding is the default (AKA https://en.wikipedia.org/wiki/Rounding#Round_half_to_even)
import math


math.ceil(1.5)  # 2
math.ceil(2.5)  # 3

math.floor(1.5)  # 1
math.floor(2.5)  # 2
int(1.5)  # 1
int(2.5)  # 2

math.ceil(Decimal("1.5"))  # 2
math.floor(Decimal("2.5"))  # 2

# Context
from decimal import getcontext

getcontext()
# Context(
#   prec=28,
#   rounding=ROUND_UP,
#   Emin=-999999,
#   Emax=999999,
#   capitals=1,
#   clamp=0,
#   flags=[Inexact, FloatOperation, Rounded],
#   traps=[InvalidOperation, DivisionByZero, Overflow]
# )
from decimal import Context, Decimal, ROUND_CEILING
context = Context(rounding=ROUND_CEILING)

Decimal("0.5").quantize(Decimal("1"), context=context)  # Decimal('1')
Decimal("0.5").quantize(Decimal("0.01"), context=context)  # Decimal('0.50')

# Special values
Decimal("infinity")
Decimal("-infinity")
Decimal("NaN")

float('infinity') # inf
float('-infinity')  # -inf
float('NaN')  # nan

float('infinity') > 5

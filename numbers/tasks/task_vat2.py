# Apply 23% VAT, round up the result
from decimal import Decimal


net_price = Decimal("117.21")
gross_price = net_price

assert gross_price == 144.17
print("OK")

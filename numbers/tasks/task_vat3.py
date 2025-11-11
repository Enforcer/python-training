# Apply 23% VAT, round up the result
from decimal import Decimal


net_price = Decimal("32.50")
gross_price = net_price

assert gross_price == 34
print("OK")

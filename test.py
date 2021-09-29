import decimal

print(42143.63)


print(decimal.Decimal('0.15')/decimal.Decimal('12'))

print(20000*(1+0.15/12)**60)
print(20000*(1+decimal.Decimal('0.15')/12)**60)
print((20000*(100+decimal.Decimal(1.25))**60) / 100**60)




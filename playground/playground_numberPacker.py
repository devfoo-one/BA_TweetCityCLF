PRECISION = 4
data = (0.1234567890, 0.23456789, 2.3, 9.99999999999)

print("packing", data)
pack = 0
for i, val in enumerate(data):
    val_trimmed = int(val* (10 ** PRECISION))
    val_final = val_trimmed * (10 ** ((PRECISION+1) * i))
    pack += val_final

print("unpacking", pack)
for i in range(3,-1,-1):
    factor = 10 ** ((PRECISION+1)*i)
    val_trimmed = int(pack / factor)
    pack -= val_trimmed * factor
    val_final = val_trimmed / 10 ** PRECISION
    print(val_final)

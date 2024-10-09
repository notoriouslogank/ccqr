WALLS = ['N','S','E','W']
RACKS = range(1,15)
SLOTS = range(1,64)
delimiter = "-"

for wall in WALLS:
    for rack in RACKS:
        for slot in SLOTS:
            print(f"{wall}{delimiter}{rack}{delimiter}{slot}")

prices = [14.25, 65.32, 12.65, 45.65, 23.52, 65.97, 40.45, 25.87, 60.35, 26.87, 36.63, 23.12, 50.32, 32.73, 10.91,]
new_list = []

for price in prices:
    roubles = int(price)
    kop = round((price - roubles) * 100)
    new_list.append(f"{roubles} руб {kop:02d} коп")
print(", ".join(new_list))


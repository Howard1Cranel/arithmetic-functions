import math

a1 = float(input("Введите a1: "))

z1 = 2 * math.sin(3 * math.pi - 2 * a1) ** 2 * math.cos(5 * math.pi + 2 * a1) ** 2
z2 = (1 / 4) - (1 / 4) * math.sin((5 / 2) * math.pi - 8 * a1 )

print(f"Вывод a1: {z1}")
print(f"Вывод a1: {z2}")

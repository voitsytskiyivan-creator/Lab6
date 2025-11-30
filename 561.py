to_meters = {
    "mile": 1609,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}
line = input("Введіть величину з одиницями (наприклад, 15.5 foot in mile): ").split()
value = float(line[0])
unit_from = line[1]
unit_to = line[3]
meters = value * to_meters[unit_from]
result = meters / to_meters[unit_to]
print(f"Переведена величина: {result:.2e}")
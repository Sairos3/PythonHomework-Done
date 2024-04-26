'''
1.      BMI-Rechner -
        es ist eine Funktion zur Berechnung des BMI zu erstellen. 
        Der BMI errechnet sich nach der Formel
            BMI = Körpergewicht in kg / (Körpergröße in m * Körpergröße in m)
        Die Funktion ist mit verschiedenen Werten zu testen.

2.      Umfang und Fläche eines Rechtecks -
        zur Berechnung des Umfangs und der Fläche eines Rechtecks
        sind zwei Funktionen zu definieren.
        Die Funktionen sind mit verschiedenen Werten zu testen.
'''
# Units
length = 4  # Meters
width = 7   # Meters

# Calculate area 4*7
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Calculate the perimeter 2*(4+7)
def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Funktion
area_result = calculate_rectangle_area(length, width)
print(f"Area: {area_result} square meters")

# OR Print
print('Area:', calculate_rectangle_area(length, width), 'square meters')

# Funktion
perimeter_result = calculate_rectangle_perimeter(length, width)
print(f"Perimeter: {perimeter_result} square meters")

# OR Print
print(f'Perimeter:', calculate_rectangle_perimeter(length, width), 'square meters')
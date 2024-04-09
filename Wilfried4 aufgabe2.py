def calc_kapital(Anfangskapital, prozent, years):
    # Calculate the end capital after the specified number of years
    for year in range(1, years + 1):
        Anfangskapital = Anfangskapital * ((prozent / 100) + 1)
    return Anfangskapital

# Get user inputs for initial capital (ak) and interest rate (p)
Anfangskapital = float(input("Geben Sie das Anfangskapital ein (in Euro): "))
prozent = float(input("Geben Sie den Zinssatz in Prozent ein: "))
years = int(input("Geben Sie die Anzahl der Jahre ein: "))

# Calculate end capital after the specified number of years
end_kapital = calc_kapital(Anfangskapital, prozent, years)

# Print the result with two decimal places
print(f"Endkapital nach {years} Jahren: {end_kapital:.2f} €")
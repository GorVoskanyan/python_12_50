class Converter:
    units = {
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.344,
        'kilometers': 1000,
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    
    def __init__(self, distance, unit):
        self.m = distance * Converter.units[unit]
        self.unit = unit
        
    def inches(self):
        return self.m / Converter.units['inches']
    
    def feet(self):
        return self.m / Converter.units['feet']
    
    def millimeters(self):
        return self.m / Converter.units['millimeters']
    
    def yards(self):
        return self.m / Converter.units['yards']

    def miles(self):
        return self.m / Converter.units['miles']
    
    def kilometers(self):
        return self.m / Converter.units['kilometers']
    
    def centimeters(self):
        return self.m / Converter.units['centimeters']
    
    def meters(self):
        return self.m / Converter.units['meters']
        
        
distance = float(input('Enter distance: '))
unit = input('Enter unit: ')
converter = Converter(distance=distance, unit=unit)


while True:
    choice = input(
        '1. Inches\n2. Feet\n3. Yards\n4. Miles\n5. Kilometers'
        '\n6. Meters\n7. Centimeters\n8. Millimeters\n9. Exit\nSelect > '
        )
    
    if choice == '9':
        print('Bye bye')
        break
    elif choice == '1':
        print(round(converter.inches(), 2), 'inches')
    elif choice == '2':
        print(round(converter.feet(), 2), 'feets')
    elif choice == '3':
        print(round(converter.yards(), 2), 'yards')
    elif choice == '4':
        print(round(converter.miles(), 2), 'miles')
    elif choice == '5':
        print(round(converter.kilometers(), 2), 'km')
    elif choice == '6':
        print(round(converter.meters(), 2), 'm')
    elif choice == '7':
        print(round(converter.centimeters(), 2), 'cm')
    elif choice == '8':
        print(round(converter.millimeters(), 2), 'mm')
    else:
        print('Invalid choice')
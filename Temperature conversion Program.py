def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def get_valid_temperature():
    """Get a valid temperature input from user"""
    while True:
        try:
            temp = float(input("Enter the temperature value: "))
            return temp
        except ValueError:
            print("Please enter a valid number.")

def get_valid_unit():
    """Get a valid unit input from user"""
    valid_units = ['C', 'F', 'K']
    while True:
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        if unit in valid_units:
            return unit
        else:
            print("Please enter a valid unit: C, F, or K")

def convert_temperature(temp, unit):
    """Convert temperature from one unit to the other two units"""
    if unit == 'C':
        # Convert from Celsius
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        return fahrenheit, kelvin, 'F', 'K'
    
    elif unit == 'F':
        # Convert from Fahrenheit
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        return celsius, kelvin, 'C', 'K'
    
    elif unit == 'K':
        # Convert from Kelvin
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        return celsius, fahrenheit, 'C', 'F'

def main():
    """Main program function"""
    print("=" * 50)
    print("      TEMPERATURE CONVERTER")
    print("=" * 50)
    print("This program converts temperatures between Celsius, Fahrenheit, and Kelvin.")
    print()
    
    while True:
        try:
            # Get temperature and unit from user
            temperature = get_valid_temperature()
            unit = get_valid_unit()
            
            # Validate physical limits
            if unit == 'K' and temperature < 0:
                print("Error: Kelvin temperature cannot be negative!")
                continue
            elif unit == 'C' and temperature < -273.15:
                print("Error: Celsius temperature cannot be below -273.15°C (absolute zero)!")
                continue
            elif unit == 'F' and temperature < -459.67:
                print("Error: Fahrenheit temperature cannot be below -459.67°F (absolute zero)!")
                continue
            
            # Convert temperature
            conv1, conv2, unit1, unit2 = convert_temperature(temperature, unit)
            
            # Display results
            print("\n" + "=" * 40)
            print("CONVERSION RESULTS:")
            print("=" * 40)
            print(f"Original: {temperature}°{unit}")
            print(f"Converted to {unit1}: {conv1:.2f}°{unit1}")
            print(f"Converted to {unit2}: {conv2:.2f}°{unit2}")
            print("=" * 40)
            
            # Ask if user wants to continue
            again = input("\nDo you want to convert another temperature? (y/n): ").lower()
            if again not in ['y', 'yes']:
                print("Thank you for using the Temperature Converter!")
                break
            print()
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
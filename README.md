# Temperature_Conversion_Program

A simple yet robust Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales.

## Features

- ✅ Convert between all three temperature scales (Celsius, Fahrenheit, Kelvin)
- ✅ User-friendly command-line interface
- ✅ Input validation and error handling
- ✅ Physical temperature limits validation (prevents below absolute zero)
- ✅ Multiple conversions in one session
- ✅ Clean, formatted output display

## How It Works

The program prompts the user to:
1. Enter a temperature value
2. Specify the original unit of measurement (C, F, or K)
3. View the converted values in the other two units

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/temperature-converter.git
```

2. Navigate to the project directory:
```bash
cd temperature-converter
```

3. Run the program:
```bash
python temperature_converter.py
```

## Requirements

- Python 3.x (no external dependencies required)

## Usage Examples

### Example 1: Converting from Celsius
```
Enter the temperature value: 25
Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): C

========================================
CONVERSION RESULTS:
========================================
Original: 25.0°C
Converted to F: 77.00°F
Converted to K: 298.15K
========================================
```

### Example 2: Converting from Fahrenheit
```
Enter the temperature value: 100
Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): F

========================================
CONVERSION RESULTS:
========================================
Original: 100.0°F
Converted to C: 37.78°C
Converted to K: 310.93K
========================================
```

### Example 3: Converting from Kelvin
```
Enter the temperature value: 273.15
Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): K

========================================
CONVERSION RESULTS:
========================================
Original: 273.15°K
Converted to C: 0.00°C
Converted to F: 32.00°F
========================================
```

## Conversion Formulas

The program uses the following standard conversion formulas:

- **Celsius to Fahrenheit**: °F = (°C × 9/5) + 32
- **Celsius to Kelvin**: K = °C + 273.15
- **Fahrenheit to Celsius**: °C = (°F - 32) × 5/9
- **Fahrenheit to Kelvin**: K = ((°F - 32) × 5/9) + 273.15
- **Kelvin to Celsius**: °C = K - 273.15
- **Kelvin to Fahrenheit**: °F = ((K - 273.15) × 9/5) + 32

## Error Handling

The program includes comprehensive error handling for:

- **Invalid input**: Non-numeric temperature values
- **Invalid units**: Units other than C, F, or K
- **Physical limits**: Temperatures below absolute zero
  - Kelvin: Cannot be negative
  - Celsius: Cannot be below -273.15°C
  - Fahrenheit: Cannot be below -459.67°F

## Program Structure

```
temperature_converter.py
├── celsius_to_fahrenheit()    # Convert Celsius to Fahrenheit
├── celsius_to_kelvin()        # Convert Celsius to Kelvin
├── fahrenheit_to_celsius()    # Convert Fahrenheit to Celsius
├── fahrenheit_to_kelvin()     # Convert Fahrenheit to Kelvin
├── kelvin_to_celsius()        # Convert Kelvin to Celsius
├── kelvin_to_fahrenheit()     # Convert Kelvin to Fahrenheit
├── get_valid_temperature()    # Input validation for temperature
├── get_valid_unit()          # Input validation for unit
├── convert_temperature()      # Main conversion logic
└── main()                    # Main program loop
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Author

Created by Amandeep Pradhan

## Acknowledgments

- Thanks to the physics community for the standard temperature conversion formulas
- Inspired by the need for a simple, reliable temperature conversion tool

---

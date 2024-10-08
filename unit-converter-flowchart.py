def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Unit Converter")
    
    while True:
        print("\nSelect the type of conversion:")
        print("1. Distance")
        print("2. Temperature")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        
        if choice == '1':
            print("\nDistance Conversion")
            value = float(input("Enter the value: "))
            unit = input("Enter the unit (m for meters, km for kilometers): ").lower()
            
            if unit == 'm':
                result = meters_to_kilometers(value)
                print(f"{value} meters is equal to {result} kilometers")
            elif unit == 'km':
                result = kilometers_to_meters(value)
                print(f"{value} kilometers is equal to {result} meters")
            else:
                print("Invalid unit. Please use 'm' for meters or 'km' for kilometers.")
        
        elif choice == '2':
            print("\nTemperature Conversion")
            value = float(input("Enter the temperature: "))
            unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()
            
            if unit == 'C':
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C is equal to {result}°F")
            elif unit == 'F':
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F is equal to {result}°C")
            else:
                print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

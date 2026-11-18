# physic formula
# 1. CALCULATION OF LINEAR MOMENTUM
def linear_momentum():
    mass = float(input("Enter mass in kg: "))
    velocity = float(input("Enter velocity in m/s: "))

    momentum = mass * velocity
    print("Linear Momentum =", momentum, "kg m/s")


# 2. CALCULATION OF PULLEY EFFICIENCY
def pulley_efficiency():
    useful_work = float(input("Enter useful work done in Joules: "))
    input_work = float(input("Enter input work in Joules: "))

    if input_work > 0:
        efficiency = (useful_work / input_work) * 100
        print("Pulley Efficiency =", efficiency, "%")
    else:
        print("Input work must be greater than zero")


# 3. CALCULATION OF OPTICAL POWER
def optical_power():
    focal_length = float(input("Enter focal length in meters: "))

    if focal_length != 0:
        power = 1 / focal_length
        print("Optical Power =", power, "Diopters")
    else:
        print("Focal length cannot be zero")


# 4. CALCULATION OF KELVIN TEMPERATURE
def kelvin_temperature():
    celsius = float(input("Enter temperature in Celsius: "))

    kelvin = celsius + 273.15
    print("Temperature in Kelvin =", kelvin, "K")


# 5. CALCULATION OF PRESSURE IN A LIQUID
def liquid_pressure():
    density = float(input("Enter liquid density in kg/m3: "))
    gravity = float(input("Enter gravitational acceleration: "))
    depth = float(input("Enter depth in meters: "))

    pressure = density * gravity * depth
    print("Liquid Pressure =", pressure, "Pascals")


# MAIN PROGRAM
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Linear Momentum")
    print("2. Pulley Efficiency")
    print("3. Optical Power")
    print("4. Kelvin Temperature")
    print("5. Liquid Pressure")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        linear_momentum()
    elif choice == "2":
        pulley_efficiency()
    elif choice == "3":
        optical_power()
    elif choice == "4":
        kelvin_temperature()
    elif choice == "5":
        liquid_pressure()
    else:
        print("Invalid selection. Choose between 1 and 5.")

    again = input("\nWould you like to perform another operation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break



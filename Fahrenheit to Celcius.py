while True:
    menu = int(input("1) fahrenheit to celsius  2) celsius to fahrenheit  3) exit : "))

    if menu == "1":
        fahrenheit = float(input("Enter temperature in fahrenheit : "))
        celsius = (fahrenheit - 32.0) * (5.0/9.0)
        print(f"{fahrenheit:.2f} degrees Farhrenheit is {celsius:.2f} degrees Celsius.")
    elif menu == "2":
        celsius = float(input("Enter temperature in celsius : "))
        fahrenheit = (celsius * 9.0 / 5.0) + 32
        print(f"{celsius:.2f} degrees celsius is {fahrenheit:.2f} degrees fahrenheit.")
    elif menu == 3:
        break

    else:
        print("Please choose from the given menu.")

print("Program finished!")






def hexadecimal_to_decimal(hexadecimal_number):
    return int(hexadecimal_number, 16)

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number).replace("0x", "")

def main():
    print("Bienvenido al conversor de hexadecimal a decimal y viceversa.")
    choice = input("Selecciona la conversión (1 para hexadecimal a decimal, 2 para decimal a hexadecimal): ")

    if choice == '1':
        hexadecimal_input = input("Ingresa un número hexadecimal: ")
        decimal_result = hexadecimal_to_decimal(hexadecimal_input)
        print(f"El número decimal equivalente es: {decimal_result}")
    elif choice == '2':
        decimal_input = int(input("Ingresa un número decimal: "))
        hexadecimal_result = decimal_to_hexadecimal(decimal_input)
        print(f"El número hexadecimal equivalente es: {hexadecimal_result}")
    else:
        print("Selección no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
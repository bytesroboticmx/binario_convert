#Autor> PhD Aldo González Vázquez
#echa> 24/11/2023
#Descripción> Programa que convierte un número octal a decimal y viceversa.
def octal_to_decimal(octal_number):
    return int(octal_number, 8)

def decimal_to_octal(decimal_number):
    return oct(decimal_number).replace("0o", "")

def main():
    print("Bienvenido al conversor de octal a decimal y viceversa.")
    choice = input("Selecciona la conversión (1 para octal a decimal, 2 para decimal a octal): ")

    if choice == '1':
        octal_input = input("Ingresa un número octal: ")
        decimal_result = octal_to_decimal(octal_input)
        print(f"El número decimal equivalente es: {decimal_result}")
    elif choice == '2':
        decimal_input = int(input("Ingresa un número decimal: "))
        octal_result = decimal_to_octal(decimal_input)
        print(f"El número octal equivalente es: {octal_result}")
    else:
        print("Selección no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
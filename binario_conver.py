#Autor: PhD Aldo Gonzalez Vazquez
#24/11/2023
#Descripción: Programa que convierte un número decimal a binario y viceversa.

def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b", "")

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def main():
    print("Conversor de decimal a binario y viceversa.")
    choice = input("Escribe la opcion (1 para decimal a binario, 2 para binario a decimal): ")

    if choice == '1':
        decimal_input = int(input("Ingresa un número decimal: "))
        binary_result = decimal_to_binary(decimal_input)
        print(f"El número binario equivalente es: {binary_result}")
    elif choice == '2':
        binary_input = input("Ingresa un número binario: ")
        decimal_result = binary_to_decimal(binary_input)
        print(f"El número decimal equivalente es: {decimal_result}")
    else:
        print("Selección no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
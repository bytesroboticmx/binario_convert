#Autor> PhD Aldo González Vázquez
#Fecha> 24/11/2023
#Descripción> Programa que convierte un código binario a ASCII y viceversa.
def binary_to_ascii(binary_string):
    ascii_text = ''.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    return ascii_text

def ascii_to_binary(ascii_text):
    binary_string = ''.join(format(ord(char), '08b') for char in ascii_text)
    return binary_string

def main():
    print("Bienvenido al conversor de código binario a ASCII y viceversa.")
    choice = input("Selecciona la conversión (1 para binario a ASCII, 2 para ASCII a binario): ")

    if choice == '1':
        binary_input = input("Ingresa un código binario: ")
        ascii_result = binary_to_ascii(binary_input)
        print(f"El texto ASCII equivalente es: {ascii_result}")
    elif choice == '2':
        ascii_input = input("Ingresa un texto ASCII: ")
        binary_result = ascii_to_binary(ascii_input)
        print(f"El código binario equivalente es: {binary_result}")
    else:
        print("Selección no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
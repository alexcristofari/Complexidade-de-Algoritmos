import sys

def calcular_tamanho_memoria(objeto):
    return sys.getsizeof(objeto)

def main():
    palavra = input("Digite uma palavra: ")

    numero_caracteres = len(palavra)

    tamanho_memoria = calcular_tamanho_memoria(palavra)

    print(f"A palavra '{palavra}' possui {numero_caracteres} caracteres.")
    print(f"Tamanho em memória: {tamanho_memoria} bytes.")

if __name__ == "__main__":
    main()

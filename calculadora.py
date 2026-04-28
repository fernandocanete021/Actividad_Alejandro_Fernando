import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def logaritmo_neperiano(a):
    return math.log(a)

def mostrar_menu():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Logaritmo neperiano")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                resultado = sumar(a, b)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: debes introducir números válidos.")

        elif opcion == "2":
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                resultado = restar(a, b)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: debes introducir números válidos.")

        elif opcion == "3":
            try:
                a = float(input("Introduce un número positivo: "))
                if a <= 0:
                    print("Error: el logaritmo neperiano solo está definido para números positivos.")
                else:
                    resultado = logaritmo_neperiano(a)
                    print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: debes introducir un número válido.")

        elif opcion == "0":
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

        print()  # Línea en blanco para separar iteraciones

if __name__ == "__main__":
    main()

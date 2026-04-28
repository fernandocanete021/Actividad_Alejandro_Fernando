import math

def sumar(a, b):
    return a + b

def restar_potencias(a, b):
    # Aquí restamos a elevado a b menos b elevado a a
    # O puedes simplemente hacer (a**b) - algo, según lo que necesites
    return (a ** b) - (b ** a)

def logaritmo_neperiano(a):
    return math.log(a)

def mostrar_menu():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar Potencias (a^b - b^a)")
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
                a = float(input("Introduce la base 'a': "))
                b = float(input("Introduce el exponente 'b': "))
                resultado = restar_potencias(a, b)
                print(f"Resultado de a^b - b^a: {resultado}")
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

        print()

if __name__ == "__main__":
    main()

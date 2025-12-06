import math

PI = 3.141592

def calcular_circunferencia(radio):

    circunferencia = 2 * PI * radio
    
    print("\n" + "*" * 40)
    print(f"CÁLCULO PARA RADIO: {radio}")
    print(f"Valor de Pi utilizado: {PI}")
    print(f"RESULTADO: La circunferencia es {circunferencia:.4f}")
    print("*" * 40 + "\n")

def mostrar_menu():
    """Muestra las opciones disponibles al usuario"""
    print("--- MENÚ DE CÁLCULO DE CIRCUNFERENCIAS ---")
    print("1. Calcular con Radio de 3")
    print("2. Calcular con Radio de 8")
    print("3. Calcular con Radio de 10")
    print("4. Ingresar un radio personalizado")
    print("5. Salir")
    print("-" * 42)


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de su opción: ")

        if opcion == "1":
            calcular_circunferencia(3)
        elif opcion == "2":
            calcular_circunferencia(8)
        elif opcion == "3":
            calcular_circunferencia(10)
        elif opcion == "4":
            try:
                radio_usuario = float(input("Ingrese el valor del radio: "))
                calcular_circunferencia(radio_usuario)
            except ValueError:
                print("\nERROR: Por favor ingrese un número válido.\n")
        elif opcion == "5":
            print("\nSaliendo del programa... ¡Hasta luego!")
            break
        else:
            print("\n[!] Opción no válida, intente nuevamente.\n")
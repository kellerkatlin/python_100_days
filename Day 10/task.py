def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division
}

def operacion():
    acumulador = True
    num1 = float(input("Elige el primer numero: "))

    while acumulador:
        for simbolo in operaciones:
            print(simbolo)
        simbolo_operacion = input("Elige la operacion:  ")
        num2 = float(input("Elige el siguiente numero: "))
        resultado = operaciones[simbolo_operacion](num1, num2)

        print(f"{num1} {simbolo_operacion} {num2} = {resultado}")

        elegir = input(f"Escribe 'y' para continuar con {resultado}, o 'n' para iniciar otra operacion: ")
        if elegir == "y":
            num1 = resultado
        else: 
            acumulador = False
            print("\n" * 10)
            operacion()
            
operacion()
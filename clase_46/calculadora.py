#Calculadora

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
def main():    
    while True:
        print("Calculadora")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir")
        opc = input("Opcion: ")
        if opc == "5":
            break
        try:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))
            if opc == "1":
                print("Resultado: ",sumar(a,b))
            elif opc == "2":
                print("Resultado: ",restar(a,b))
            elif opc == "3":
                print("Resultado: ",multiplicar(a,b))
            elif opc == "4":
                print("Resultado: ",dividir(a,b))
            else:
                print("Opcion invalida")
        except ValueError:
            print("Error: Solo se permiten numeros")
        except Exception as e:
            print("Error: ",e)
        input("Presione Enter para continuar...")

main()
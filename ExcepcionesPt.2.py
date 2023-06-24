# múltiples excepciones y más específicas para cada caso

def dividir():

    while True:
        try:
            num1 = float(input("Digite un número -> "))
            num2 = float(input("Digite otro número -> "))
            resultado = num1/num2
            print(f"El resultado de la división es: {resultado:.2f}")

        except ValueError:
            print("Error, digite correctamente los valores numéricos")

        except ZeroDivisionError:
            print("Error -> no se puede dividir entre 0")

        else:
            break

dividir()

# Carolina EM




#Calculadora simples

# Definir operações matematicas para o usuario
def adição(x, y):
    return x + y

def subtração(x, y):
    return x + y

def multiplicação(x,y):
    return x * y

def divisão(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por 0."
    
# Definir a escolha do usuario sobre o tipo de operação matematica desejada
def calculator():
    print("Selecione a operação")
    print("1. Adição")
    print ("2. Subtração")
    print ("3. Multiplicação")
    print ("4. Divisão")

# Criar uma variavel para o usuario realizar sua escolha e definir suas funções.
    choice = input("Digite sua escolha (1/2/3/4) : ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro numero "))
        num2 = float(input("Digite o segundo numero "))

        if choice == "1":
            print(f"{num1} + {num2} = {adição(num1, num2)}")
        
        elif choice == "2":
            print(f"{num1} - {num2} = {subtração(num1, num2)}")
        
        elif choice == "3":
            print(f"{num1} * {num2} = {multiplicação(num1, num2)}")

        elif choice == "4":
            print(f"{num1} / {num2} = {divisão(num1, num2)}")

    else:
        print("Escolha Invalida")
         
# Definir a calculadora como um modulo
if __name__ == "__main__":
    calculator()

    
    

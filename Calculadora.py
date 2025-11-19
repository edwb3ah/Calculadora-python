# calculadora.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def main():
    while True:
        print("\n=== Calculadora ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        escolha = input("Escolha a operação: ")

        if escolha == "5":
            print("Saindo da calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            print("Resultado:", soma(num1, num2))
        elif escolha == "2":
            print("Resultado:", subtracao(num1, num2))
        elif escolha == "3":
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == "4":
            print("Resultado:", divisao(num1, num2))
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

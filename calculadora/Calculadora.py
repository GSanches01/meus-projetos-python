#PROJETO CALCULADORA

"""criando função"""
def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações: + - * /")
    #loop principal
    while True:
        try:   #tratamento de erros com try/except
            num1 = float(input("\nDigite o primeiro número: ")) #capturando dados
            operador = input("Digite a operação (+, -, *, /): ") #capturando dados
            num2 = float(input("Digite o segundo número: ")) #capturando dados

            if operador == "+": #estrutura condicional
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                    continue #pula o resto do código do loop e volta pro início do while
                resultado = num1 / num2
            else:
                print("Operador inválido!")
                continue

            print(f"Resultado: {num1} {operador} {num2} = {resultado}")#Formatando a saída com f-string

        except ValueError:#Caso especial: divisão por zero
            print("Digite apenas números válidos.")

        continuar = input("\nDeseja fazer outra operação? (s/n): ")#Perguntando se quer continuar
        if continuar.lower() != "s":
            print("Encerrando calculadora...")
            break


if __name__ == "__main__":
    calculadora()
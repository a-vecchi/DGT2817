saida = ''

def adicao(x, y):
    return float(x) + float(y)

def subracao(x, y):
    return float(x) - float(y)

def multiplicacao(x, y):
    return float(x) * float(y)

def divisao(x, y):
    if float(x) == 0 or float(y) == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return float(x) / float(y)

def calculadora(numero1, numero2, operacao):
    if operacao == '+' or operacao.lower() in ['adicao', 'adição', 'adiçao', 'adicão']:
        resultado = adicao(numero1, numero2)
    elif operacao == '-' or operacao.lower() in ['subtracao', 'substração', 'substraçao', 'substracão']:
        resultado = subracao(numero1, numero2)
    elif operacao == '*' or operacao.lower() in ['multiplicacao', 'multiplicação', 'multiplicaçao', 'multiplicacão']:
        resultado = multiplicacao(numero1, numero2)
    elif operacao == '/' or operacao.lower() in ['divisao', 'divisão']:
       resultado = divisao(numero1, numero2)
    else:
        resultado = 'Operação não implementada'
    return resultado

while saida.lower() != 'n':
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operacao = input('Digita a operação desejada: ')
    resultado = calculadora(numero1, numero2, operacao)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja continuar ou não executando o programa? (S/N):')

#Esta função irá dar as boas vindas e chamar a função da Calculadora
def entrar_calc():
    print('''
===========================================================

Bem Vindo(a) à sua Calculadora!! Vamos lá''')
    calculadora()

#Aqui é onde irá ser perguntado sobre o tipo de operação e dado o resultado
def calculadora():
    operacao = input('''
===========================================================

Por favor, digite o simbolo da operação que deseja efetuar:

+ (Adição)
- (Subtração)
* (Multiplicação)
/ (Divisão)

''')
#ADICAO
    if operacao == '+':
        numero_1 = int(input('\nPrimeiro número: '))
        numero_2 = int(input('Segundo número: '))
        print('''
{} + {} = {}
'''.format(numero_1, numero_2, numero_1 + numero_2))
#SUBTRACAO
    elif operacao == '-':
        numero_1 = int(input('\nPrimeiro número: '))
        numero_2 = int(input('Segundo número: '))
        print('''
{} - {} = {}
'''.format(numero_1, numero_2, numero_1 - numero_2))
#MULTIPLACACAO
    elif operacao == '*':
        numero_1 = int(input('\nPrimeiro número: '))
        numero_2 = int(input('Segundo número: '))
        print('''
{} * {} = {}
'''.format(numero_1, numero_2, numero_1 * numero_2))
#DIVISAO
    elif operacao == '/':
        numero_1 = int(input('\nPrimeiro número: '))
        numero_2 = int(input('Segundo número: '))
        print('''
{} / {} = {:.1f}
'''.format(numero_1, numero_2, numero_1 / numero_2))
#Se não for nenhuma da opções
    else:
        print('''
Insira um simbolo válido: +, -, * ou /.
''')
    continuar()

#Função para continuar ou sair da calculadora
def continuar():
    repetir_calculo = input('''
Deseja continuar? 
Digite "S" para "sim" e "N" para "não"

''' )
    if repetir_calculo .upper() == 'S':
        calculadora()
    elif repetir_calculo .upper() == 'N':
        print('Espero ter ajudado, até uma próxima! ^-^')
    else:
        continuar()

#Nunca esquecer de chamar a função para que o programa possa funcionar
entrar_calc()
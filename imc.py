def entrar_imc():
    print('''
===================================

Bem Vindo à sua Calculdaora de IMC! ''')
    imc()

def imc():
    altura = float(input('''
===================================

Sua altura: 
'''))
    peso = float(input('''
Seu peso: 
'''))
    calculo = peso / (altura * altura)

    if calculo <= 18.5:
        print('IMC: {:.1f} - Abaixo do peso'.format(calculo))
    elif calculo >= 18.6 and calculo <= 24.9:
        print('IMC: {:.1f} - Peso ideal'.format(calculo))
    elif calculo >= 25.5 and calculo <= 29.9:
        print('IMC: {:.1f} - Levemente acima do peso'.format(calculo))
    elif calculo >= 30.0 and calculo <= 34.9:
        print('IMC: {:.1f} - Obesidade grau 1'.format(calculo))
    elif calculo >= 35.5 and calculo <= 39.9:
        print('IMC: {:.1f} - Obesidade grau 2 (severa)'.format(calculo))
    else:
        print('IMC: {:.1f} - Obesidade grau 3 (mórbida)'.format(calculo))
    repetir()

def repetir():
    continuar = input('''
Deseja continuar?
(Digite "S" para "sim" e "N" para "não")
''')
    if continuar .upper() == 'S':
        imc()
    elif continuar .upper() == 'N':
        print('Espero ter ajudado, até uma próxima! ^-^')
    else:
        repetir()


entrar_imc()
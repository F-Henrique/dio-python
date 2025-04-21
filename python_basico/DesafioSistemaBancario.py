saldoInicial = float(input('Digite o saldo atual.'))

valorBanco = saldoInicial 
totalSaques=0
limite=500
MAXIMOSAQUES=3
operacoesB = []

textoInicial="""
    Escreva a operacao que deseja realizar:                             
      [D]epositar
      [S]aque
      Visualizar [E]xtrato
      [Q]uit
    : """

while True:
    
    operacaoBancaria = input(textoInicial)
    
    if len(operacaoBancaria) > 1 or  isinstance(operacaoBancaria, (int, float)):
        print('erro')
    
    else:
        match operacaoBancaria.upper():
            
            case "D":
             
                valorDeposito = float(input('Qual o valor a ser depositado? '))
                
                # operacoesB.append('Depos: R$' +str(valorDeposito))
                operacoesB.append(f'Depos: R${valorDeposito:.2f}')

                            #
                valorBanco= valorBanco + valorDeposito
                       
            case "S":
                
                
               
                if totalSaques < MAXIMOSAQUES: 
                
                    while totalSaques <= MAXIMOSAQUES:
                            
                        valorSaque = float(input('Qual o valor a ser sacado? '))
                    
                        if valorSaque > valorBanco:
                            print('o valor solicitado e menor que o saldo atual')
                            
                        elif valorSaque <= limite:
                             
                             totalSaques = totalSaques + 1
                            
                            #  operacoesB.append('Saque: R$' +str(valorSaque))
                             operacoesB.append(f'Saque: R$ {valorSaque:.2f}')
                            #  print(f'Saque :R$ {valorSaque:.2f}')
                             valorBanco = valorBanco - valorSaque
                             
                        else:
                             print('')
                             print('O valor a ser sacado e maior que o limite permitido.')
                             
                        break
                             
                else:
                    print('')
                    print('Operacoes de saque sao limitadas a 3 por execucao.')
                    
            case "E":
                print('')
                print('-----------------')
                
                for operacao in operacoesB:
                    print(operacao)

                print('-----------------')
                print(f'saldo atual de: R$ {valorBanco:.2f}')
    
            case "Q": break
            
            case _:
                
                print('deu ruim.')

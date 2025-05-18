
for i in range(1):#funções

    for i in range(1):#suporte

        def completa_String(frase,tamanho,sep = ' '):

            while len(frase) < tamanho:
                frase = frase + sep

            return frase

        #-----------------------
        def formatar_cpf(cpf):

            int_cpf = ''.join(filter(str.isdigit, cpf))
                
            while len(int_cpf)<11:
                int_cpf = '0' + int_cpf            
            # return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return int_cpf
    
    for i in range(1):#ações de conta
        def funcaoDeposito(int_valorBanco,int_valorDeposito,operacoes, /):
                    
            operacoes.append(f'Depos: R$ {int_valorDeposito:.2f}')
            int_valorBanco += int_valorDeposito
            return int_valorBanco
        
        def funcaoSaque(*, valorBanco, valorSaque, limite, totalSaques, MAXIMOSAQUES,operacoes):
                    
            if totalSaques < MAXIMOSAQUES: 
            
                while totalSaques <= MAXIMOSAQUES:
                    
                    if valorSaque > valorBanco:
                        print('o valor solicitado e menor que o saldo atual')
                        return None,None
                        
                    elif valorSaque <= limite:
                            
                            totalSaques = totalSaques + 1
                            operacoes.append(f'Saque: R$ {valorSaque:.2f}')
                            return totalSaques, valorSaque
                    else:
                            print('')
                            print('O valor a ser sacado e maior que o limite permitido.')
                            return None,None
                    
                            
            else:
                print('')
                print('Operacoes de saque sao limitadas a 3 por execucao.')
                return None,None
        
        def funcaoExtrato(int_valorBanco,operacoesB):
            
            print('')
            tamanhoTotal = len(f'| saldo atual de: R$ {int_valorBanco:.2f} |')
            cabecalhoLista = completa_String('====== EXTRATO ',tamanhoTotal - 3,'=')
            print(f'|{cabecalhoLista}|')
            linhaBranco = completa_String(' ',tamanhoTotal - 3)
            print(f'|{linhaBranco}|')

            if operacoesB:      

                for operacao in operacoesB:
                    
                    frase1 = f'|- {operacao}'
                    
                    frase2 = completa_String(frase1,tamanhoTotal-2)
                    if len(frase1) < tamanhoTotal - 2:
                        frase3 = frase2 + '|'
                    
                    else: frase3 = frase2

                    print(frase3)

                    entrelinhas = completa_String('-',tamanhoTotal - 3,'-')
                    print(f'|{entrelinhas}|')
            else:
                
                    entrelinhas = completa_String('-',tamanhoTotal - 3,'-')
                    print(f'|{entrelinhas}|')

            linhaFinal = completa_String('=',tamanhoTotal - 3,'=')  
            print(f'|{linhaFinal}|')
            
            print(f'| saldo atual de: R$ {int_valorBanco:.2f}|')
            print(f'|{entrelinhas}|')
    
    for i in range(1):#usuário        
        def perguntasCadastroUsuario(int_cpf):        
                
                
                temp_ids=[]
                for usuario in usuarios:
                    temp_ids.append(usuario["id"])

                proximo_id = 1 + max(temp_ids)
                
                print('Digite "exit" para cancelar.')
                nomeUsuario = input('Digite nome completo: ')                
                if nomeUsuario == 'exit':
                    return None
                
                senha = input('Digite uma senha para seu usuário: ')                
                if senha == 'exit':
                    return None
                
                print('Digite "exit" para cancelar.')
                
                for ia1 in range(1):#range de perguntas para endereço do usuário

                    data_nasc= input('Digite a data de nascimento do usuário? (formato: dd-mm-aaaa)')
                    if data_nasc == 'exit':
                        return None
                    
                    enderecoUsuario5 = input('Digite a sigla do Estado do usuário? ')
                    if enderecoUsuario5 == 'exit':
                        return None
                
                    print('Digite "exit" para cancelar.')
                
                    enderecoUsuario4 = input('Digite a cidade do usuário? ')
                    if enderecoUsuario4 == 'exit':
                        return None
                    
                    enderecoUsuario3 = input('Digite o bairro do usuário? ')
                    if enderecoUsuario3 == 'exit':
                        return None
                    
                    print('Digite "exit" para cancelar.')

                    enderecoUsuario2 = str(input('Digite o nº da residência do usuário? '))
                    if enderecoUsuario2 == 'exit':
                        return None
                    
                    enderecoUsuario1 = input('Digite o logradouro (sem número) do usuário? ')
                    if enderecoUsuario1 == 'exit':
                        return None
                    
                enderecoUsuario = enderecoUsuario1 +', '+ enderecoUsuario2 +' - '+ enderecoUsuario3 +' - '+ enderecoUsuario4 +'/'+ enderecoUsuario5

                usuarios.append({"id": proximo_id,
                    "cpf": int_cpf,
                    "nome": nomeUsuario,
                    "senhaUsuario": senha,
                    "data_nasc": data_nasc,
                    "endereço": enderecoUsuario,
                    "contas":[]
                                })
                return True
        
        def funcaoCadastroUsuario():
            
            cpfUsuario = input('Digite cpf:')
            # Remove tudo que não é dígito
            int_cpf = formatar_cpf(cpfUsuario)
           
            if funcaoLocalizarUsuario(int_cpf):

                defineCpf = input('Você deseja criar uma nova conta para este cpf? (Y/N) ')
                
                if defineCpf.upper() == 'Y':

                    senhaUsuario = input('Autorize a criação da conta através da senha do usuário: ')
                    
                    for usuario in usuarios:
                        if usuario['cpf'] == int_cpf:

                            if usuario['senhaUsuario'] == senhaUsuario:
                                contaNova = funcaoCriarConta(int_cpf)
                                usuario["contas"].append(contaNova)
                                return True
                            else:
                                print('senha incorreta.')
                    return None
                else:
                    return None

            else:

                print('Esse cpf não está cadastrado. Efetuaremos seu cadastro agora.')
                
                if perguntasCadastroUsuario(int_cpf):
                    return True

        def funcaoLocalizarUsuario(cpf):
            
            for usuario in usuarios:
                if cpf == usuario["cpf"]:
                    return True
            
            return None
        
        def ControlaAcessoUsuario():
            
            cpfUsuario = input('Digite cpf:')
            # Remove tudo que não é dígito
            int_cpf = formatar_cpf(cpfUsuario)
           
            if funcaoLocalizarUsuario(int_cpf):
                
                for usuario in usuarios:
                    if int_cpf == usuario['cpf']:
                        var_QuantContas=len(usuario['contas'])
                        if var_QuantContas == 1:
                            contaUsuario = usuario['contas'][0]
                        else:
                            contaUsuario = input('Este usuário possui mais de uma conta. Digite a conta que deseja realizar a operação : ')
                        
                        break
                
                
                if funcaoLocalizarConta(contaUsuario):    

                    for usuario in usuarios:
                        if int_cpf == usuario['cpf']:
                            if contaUsuario in usuario['contas']:
                                return contaUsuario, True
                        
                    
                    print('O usuário em questão não tem acesso à conta indicada.')
                    return None, None
                else:
                    print('Essa conta não foi reconhecida.')
                    return None, None
            
            else:
                print('Esse cpf não está cadastrado. É necessário ter cadastro para seguir com esta operação.')
                return None, None
           
        def funcaoListarUsuarios(usuarios):

            tamanhoTotal=0

            if usuarios:

                for usuario in usuarios:

                    tamanhoTotal1 = len(f'| Nome: {usuario["nome"]} -/- cpf: {usuario["cpf"]} |')
                    tamanhoTotal2 = len(f'| endereço: {usuario["endereço"]} |')
                   
                    if tamanhoTotal1 > tamanhoTotal2:
                        if tamanhoTotal1 > tamanhoTotal:
                            tamanhoTotal = tamanhoTotal1
                    else:                    
                        if tamanhoTotal2 > tamanhoTotal:
                            tamanhoTotal = tamanhoTotal2
                    
                
                print('')
                cabecalhoLista = completa_String('===== lista de usuários ',tamanhoTotal-2,'=')
                print(f'|{cabecalhoLista}|')
                linhaBranco = completa_String(' ',tamanhoTotal-2)
                print(f'|{linhaBranco}|')

                linhaFinal = completa_String('=',tamanhoTotal-2,'=')  
                print(f'|{linhaFinal}|')

                for usuario in usuarios:
                    
                    frase1 = f'Nome: {usuario["nome"]} -/- cpf: {usuario["cpf"]}'
                    
                    frase2 = completa_String(frase1,tamanhoTotal-3)
                    if len(frase1) < tamanhoTotal-3:
                        frase3 = frase2 + '|'
                    
                    else: frase3 = frase2

                    print('| ' + frase3)
                    ##########
                    frase1 = f'Endereço: {usuario["endereço"]}'
                    
                    frase2 = completa_String(frase1,tamanhoTotal-3)
                    if len(frase1) < tamanhoTotal-3:
                        frase3 = frase2 + '|'
                    
                    else: frase3 = frase2

                    print('| ' + frase3)
                    
                    frase3 = f'data_nascimento: {usuario["data_nasc"]}'
                    frase4 = completa_String(frase3,tamanhoTotal-4)
                    print(f'|  {frase4}|')

                    frase5 = f'conta associada:'
                    frase6 = completa_String(frase5,tamanhoTotal-4)
                    print(f'|  {frase6}|')

                    for conta in usuario["contas"]:
                        frase7 = f'  {conta}'
                        frase8 = completa_String(frase7,tamanhoTotal-4)
                        print(f'|  {frase8}|')
                    
                    #############
                    entrelinhas = completa_String('-',tamanhoTotal-2,'-')
                    
                    print(f'|{entrelinhas}|')
                    
                    print(f'|{linhaFinal}|')
                        
            else:
                print('')
                cabecalhoLista = completa_String('==== lista de usuários ====',tamanhoTotal,'=')
                print(f'|{cabecalhoLista}|')
                print(f'|Nenhum usuário cadastrado. |')
        
        def funcaoExpoeUsuario(): 
            
            cpfUsuario = input('Digite cpf:')
            # Remove tudo que não é dígito
            int_cpf = formatar_cpf(cpfUsuario)
           
            if funcaoLocalizarUsuario(int_cpf):
                
                textoNovo =""" 
                O que deseja alterar:                             
    [N]ome do usuário
    [D]ata de nascimento
    [E]ndereço
    [S]enha
    [Q]uit
    : 
    """
                
                while True:
                    
                    operacaoAlteracao = input(textoNovo)
                    
                    if isinstance(operacaoAlteracao, (int, float)):
                        print('erro')
                    
                    else:
                        
                        if operacaoAlteracao.upper()=='Q':
                            return
                        
                        senhaUsuario = input('Digite a senha cadastrada: ')
                        for usuario in usuarios:
                            if usuario['cpf'] == int_cpf:
                                
                                if usuario['senhaUsuario'] == senhaUsuario:
                                    
                                    match operacaoAlteracao.upper():
                                        
                                        case "N":
                                            
                                            nomeUsuario = input('Digite novo nome? ')
                                            usuario["nome"] = nomeUsuario
                                            print('Nome de usuário alterado!')
                                            break
                                                 
                                        case "D":
                                            
                                            data_nasc = input('Digite a data de nascimento corrigida: (formato: dd-mm-aaaa) ')
                                            usuario["data_nasc"] = data_nasc
                                            print('Data de nascimento do usuário alterado!')
                                            break
                                               
                                        case "E":
                                             
                                            for ia1 in range(1):#range de perguntas para endereço do usuário
                                                
                                                print('Digite "Q" para cancelar.')
                                                
                                                enderecoUsuario5 = input('Digite a sigla do Estado do usuário? ')
                                                if enderecoUsuario5 == 'Q':
                                                    break
                                            
                                                enderecoUsuario4 = input('Digite a cidade do usuário? ')
                                                if enderecoUsuario4 == 'Q':
                                                    break
                                                
                                                enderecoUsuario3 = input('Digite o bairro do usuário? ')
                                                if enderecoUsuario3 == 'Q':
                                                    break
                                                
                                                print('Digite "Q" para cancelar.')

                                                enderecoUsuario2 = str(input('Digite o nº da residência do usuário? '))
                                                if enderecoUsuario2 == 'Q':
                                                    break
                                                
                                                enderecoUsuario1 = input('Digite o logradouro (sem número) do usuário? ')
                                                if enderecoUsuario1 == 'Q':
                                                    break
                                                
                                            enderecoUsuario = enderecoUsuario1 +', '+ enderecoUsuario2 +' - '+ enderecoUsuario3 +' - '+ enderecoUsuario4 +'/'+ enderecoUsuario5

                                            usuario["endereço"] = enderecoUsuario
                                            print('Endereço do usuário alterado!')
                                            break
                                                
                                        case "S":
                                            
                                            while True:
                                                
                                                print('Digite "Q" para cancelar.')
                                                
                                                senhaUsuario2 = input('Digite nova senha: ')
                                                if senhaUsuario2 == 'Q':
                                                    break
                                                
                                                senhaUsuario3 = input('Repita a nova senha: ')
                                                if senhaUsuario3 == 'Q':
                                                    break
                                            
                                                if senhaUsuario2 == senhaUsuario3:

                                                    usuario["senhaUsuario"] = senhaUsuario3
                                                    print('Senha de usuário alterado!')
                                                    break
                                                else:
                                                    print('Senhas não correspondem!')
                                        
                                        case _:                
                                            print('Por favor, escolha uma das opções sinalizadas no menu inicial.')

                                else:
                                    print('Senha incorreta!')
                                     
                                    
            else:
                print('O cpf indicado não existe em nossa base de dados.')

    for i in range(1):#conta
        def funcaoCriarConta(cpf):

            temp_contas=[]
            #1) pegar cada conta existente dentro de contasCriadas;
            #2) pegar os números que vêm após o 0001 e antes dos 11 números finais;
            
            for conta in contasCriadas:
                
                #retirando agencia
                var_semAgencia = conta['conta'][4:]
                
                tamanhoIndice = len(var_semAgencia)-len(cpf)
                
                #retirando números do cpf
                var_ordem = var_semAgencia[:tamanhoIndice]
                
                conta_temp = int(var_ordem)
                temp_contas.append(conta_temp)
            
            conta_id = str(max(temp_contas) + 1)
            contaNova = "0001" + conta_id + cpf        
            senhaConta = input('Digite uma senha para sua conta: ')
            contasCriadas.append({"conta": contaNova,
                                "senhaconta": senhaConta,
                                'saldo':0,
                                'operacoes':[]})

            return contaNova

        def funcaoLocalizarConta(contaUsuario):
            
            for conta in contasCriadas:
                if contaUsuario == conta['conta']:
                    return True
            
            return None
    
        def ControlaAcessoConta(int_conta):  
            
            int_senha = input('Digite a senha da conta que deseja efetuar a operação:')
                        
            for conta in contasCriadas:
                if int_conta == conta['conta']:
                    if int_senha == conta['senhaconta']:
                        return int_senha,True
        
            return None, None
                
    

totalSaques=0
limite=500
MAXIMOSAQUES=3
contasCriadas = []
contasCriadas = [{'conta':'0001112345678988','senhaconta':'asdf1', 'saldo':0, 'operacoes':[]},
                 {'conta':'0001202345678988','senhaconta':'asdf2', 'saldo':0, 'operacoes':[]},
                 {'conta':'0001310345678988','senhaconta':'asdf3', 'saldo':0, 'operacoes':[]},
                 {'conta':'00011010345678988','senhaconta':'asdf10', 'saldo':0, 'operacoes':[]}
                 ]
usuarios = []
usuarios = [
    {"id": 1,"cpf": "12345678988","nome": "nomeUsuario1","senhaUsuario": "qwe1", "data_nasc": "12-01-1992",
     "endereço": "enderecoUsuario","contas":['0001112345678988']},
    {"id": 2,"cpf": "02345678988","nome": "nomeUsuario2","senhaUsuario": "qwe2", "data_nasc": "25-11-2000",
     "endereço": "enderecoUsuario","contas":['0001202345678988']},
    {"id": 3,"cpf": "10345678988","nome": "nomeUsuario3","senhaUsuario": "qwe3", "data_nasc": "14-07-1990",
     "endereço": "enderecoUsuario","contas":['0001310345678988','00011010345678988']}
]

textoInicial="""
    Escreva a operacao que deseja realizar:                             
      [Alt]erar dados de usuário
      [Cri]ar nova Conta
      [D]epositar
      Visualizar [E]xtrato
      [S]aque
      Lista de [Usu]ários
      [Q]uit
      :
     """

while True:
    
    var_Concluiu= False
    contaUsuario=''
    senhaConta='' 
    valorFinal= False 
    valorFinal2= False

    try: 

        operacaoBancaria = input(textoInicial)
    
        if isinstance(operacaoBancaria, (int, float)):
            print('erro')
        
        else:

            match operacaoBancaria.upper():
                
                case "D":
                    
                    contaUsuario, valorFinal= ControlaAcessoUsuario()
                    
                    if valorFinal:

                        senhaConta, valorFinal2 = ControlaAcessoConta(contaUsuario)
                        
                        if valorFinal2:
                            
                            valorDeposito=0

                            for conta in contasCriadas:
                                if contaUsuario == conta['conta']:
                                    if senhaConta == conta['senhaconta']:
                                        valorBanco = conta['saldo']
                                        valorDeposito = float(input('Qual o valor a ser depositado? '))
                                        novoValorBanco = funcaoDeposito(valorBanco, valorDeposito,conta['operacoes'])
                                        conta['saldo'] += novoValorBanco
                                        var_Concluiu = True
                                        break
                                    
                            
                    if var_Concluiu== True:continue
                    
                    print('')
                    print('Operação não efetuada.')

                case "S":

                    contaUsuario, valorFinal= ControlaAcessoUsuario()
                    
                    if valorFinal:
   
                        senhaConta,valorFinal2 = ControlaAcessoConta(contaUsuario)
                        
                        if valorFinal2: 
                            
                            valorSaque = 0
                            for conta in contasCriadas:
                                  
                                  if contaUsuario == conta['conta']:
                                    if senhaConta == conta['senhaconta']:
                                        
                                        valorBanco = conta['saldo']
                                        valorSaque = float(input('Qual o valor a ser sacado? '))
                            
                                        totalSaques2, novoValorBanco = funcaoSaque(valorBanco=valorBanco, valorSaque=valorSaque, 
                                          limite = limite, totalSaques = totalSaques, 
                                          MAXIMOSAQUES= MAXIMOSAQUES, operacoes = conta['operacoes'])
                                        
                                        if totalSaques2 == None:
                                            break
                                        
                                        else:
                                            totalSaques += totalSaques2
                                            if novoValorBanco:
                                                conta['saldo'] -= novoValorBanco
                                                
                                                var_Concluiu = True
                                                break
                            
                            if var_Concluiu== True:
                                print('Saque efetuado com sucesso.')
                                continue
                    print('')
                    print('Operação não efetuada.')
                        
                case "E":
                    
                    contaUsuario, valorFinal= ControlaAcessoUsuario()
                    
                    if valorFinal:

                        senhaConta, valorFinal2 = ControlaAcessoConta(contaUsuario)
                        
                        if valorFinal2: 

                            for conta in contasCriadas:
                                 if contaUsuario == conta['conta']:
                                    if senhaConta == conta['senhaconta']:
                                        valorBanco = conta['saldo']
                                        
                                        funcaoExtrato(valorBanco, conta['operacoes'])
                                        var_Concluiu= True
                                        break
                                    else:
                                        print('Senha errada.')
                                        break
                        
                        if var_Concluiu== True:
                            print('')
                            continue
                    print('')
                    print('Operação não efetuada.')
               
                case "CRI":

                    retorno=funcaoCadastroUsuario()
                    if retorno:
                        print('')
                        print('Nova conta criada!')
                    else:
                        print('ação cancelada.')
                   
                case "ALT":                
                    funcaoExpoeUsuario()
                    
                case "USU":             
                    funcaoListarUsuarios(usuarios)

                case "Q": 
                    break
                
                case _:                
                    print('Por favor, escolha uma das opções sinalizadas no menu inicial.')


    except Exception as erro: 
        print(f"Erro: {erro}")
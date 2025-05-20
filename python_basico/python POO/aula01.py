for ia1 in range(1):# aula 01
    """
    desafio bicicletaria

    obs1: métodos que não recebem argumentos em python necessitam ser 
        declarados com a classe (representada pelo 'self', abaixo); no 
        entanto, 'self' não é uma palavra reservada, mas uma convenção:
        se outra palavra fosse colocada, o python entenderia que essa 
        outra palavra é o 'self'. Logo, se um método necessitar de 
        argumentos, o primeiro obrigatoriamente será entendido como 
        'self' pelo python e só a partir do segundo será entendido 
        como argumento do método
        
    """

    class Bicicleta:
        
        def __init__(self, cor, modelo, ano, valor):
            self.cor = cor
            self.modelo = modelo
            self.ano = ano
            self.valor = valor

        def buzinar(self):
            print('buzinando')

        def parar(self):
            print('parando bicicleta')
            print('bicicleta parada')

        def correr(self):
            print('bicicleta correndo')

        #forma de listar os parâmetros da classe
        # def __str__(self):
        #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, 
        #              ano={self.ano}, valor={self.valor}'
        
        #-> uma forma dinâmica de listar os parâmetros da classe é representada abaixo:

        def __str__(self):
            #return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave,valor in self.__dict__.items()]}"
            #com o 'for' acima, retornava uma lista: [cor = cor, modelo = modelo, etc]
            #com o join abaixo, eu retiro da lista e concateno a informação, 
            # usando ', ' como separador
            return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

    # b1 = Bicicleta('vermelha','caloy',2022,400)
    # b1.buzinar()# = Bicicleta.buzinar(b1)
    # print(b1)
    # print('novo3')

    #################### fim da bicicletaria
    """
    aula de construtores e destrutores

    obs1: o método 'del' sempre existe numa classe e é executado quando
    ela se encerra (no caso abaixo, quando o programa encerrou); não 
    precisa ser explícita, exceto se quiser executar mais alguma 
    coisa ao fim da execução.

    no exemplo abaixo ao escrever 'print(c)', apareceria:
            Inicializando a classe
            Cachorro: nome = chappie, cor = amarelo, acordado = True
            removendo a instância da classe.

    ao escrever : 'print(c)' e 'c.falar()' :

            Inicializando a classe
            Cachorro: nome = chappie, cor = amarelo, acordado = True
            auau
            removendo a instância da classe.

        
    """

for ia1 in range(1):# aula 02
    class Cachorro:
        def __init__(self, nome, cor, acordado = True):
            print("Inicializando a classe")
            self.nome=nome
            self.cor=cor
            self.acordado = acordado

        def __del__(self):
            print("removendo a instância da classe.")

        def falar(self):
            print("auau")


        def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"


    def criar_cachorro():
            """ método para instanciar o objeto. a saída é:
            Inicializando a classe
            zeus
            removendo a instância da classe.
            """
            c = Cachorro('zeus', 'branco',False)
            print(c.nome)

    # criar_cachorro()

    # c= Cachorro('chappie', 'amarelo')

    # print(c)
    # c.falar()

    # print('olá')
    # del c# obriga o del da classe a agir, pq este comando encerra a instância
    # print('olá')
    # print('olá')
    # print('olá')

"""
    aula de Herança
    -> Herança Simples

    Uma classe 'Pai' pode passar suas características para 
    classe-filhas: variáveis e métodos. Serve como 'guia' do que 
    se espera para os filhos, mas isso não significa que, por ter 
    no pai, deve existir nos filhos. O que é criado nos filhos é 
    exclusivo deles. Se um filho precisar de argumentos 
    adicionais, utilizar 'super()' evita reescrever variáveis 
    que a classe pai já cobraria quando da instanciação, então 
    basta escrever o diferencial das classes-filhas

"""
for ia2 in range(1):# -> Herança Simples
    class Veiculo:
        def __init__(self, cor, placa, numero_rodas):
            self.cor = cor
            self.placa = placa
            self.numero_rodas = numero_rodas
        
        
        def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"

        def ligar_motor(self):
            print("Ligando motor")
        
    class Motocicleta(Veiculo):
        pass


    class Carro(Veiculo):
        pass


    class Caminhao(Veiculo):

        def __init__(self, cor, placa, numero_rodas, carregado):
            super().__init__(cor, placa, numero_rodas)
            self.carregado = carregado


        def esta_carregado(self):
            print(f'{ "Sim" if self.carregado else "Não"} estou carregado.')

    # m = Motocicleta('vermelha','placa1',2)
    # print(m)
    # m.ligar_motor()

    # car = Carro('vermelha','placa1',4)
    # car.ligar_motor()

    # cam = Caminhao('vermelha','placa1',18, False)
    # cam.ligar_motor()
    # cam.esta_carregado()

"""
    Herança Múltipla pode facilmente tornar o código complexo. 
    Existe uma ordem de 'execução' (da classe menor para as 
    superiores) e essa ordem pode ser demonstrada através do 
    MRO (ordem de resolução dos métodos);
    print(~nome da classe em questão~ .__mro__))



"""
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"


class Mamifero(Animal):
    # def __init__(self, nro_patas, cor_pelo):
    #     super().__init__(nro_patas)
    #     self.cor_pelo= cor_pelo

    # acima funciona para herança simples; em caso de herança 
    # múltipla, deve-se usar o conceito "*kw": deixar apenas 
    # os argumentos da classe filha (mamífero) e acrescentar "kw" como 
    # representante do que vier de classes acima:
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo= cor_pelo

class Ave(Animal):# o mesmo ocorre aqui, já que tb é 'pai' de ornitorrinco
    def __init__(self, cor_bico,**kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.mro()) #-> demonstra a ordem de execução: 
        # Ornitorrinco> Mamifero> Ave> Animal> Classes
        #saída -> [<class '__main__.Ornitorrinco'>, <class '__main__.Mamifero'>,
        #  <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]

        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico, nro_patas=nro_patas)
        # a consequência inevitável é que agora os argumentos devem 
        # ser nomeados ao instanciar o objeto

    def __str__(self):
        return super().__str__()
        # return 'Ornitorrinco'
    
# gato = Gato(4,'branco')
# print(gato)

ornt = Ornitorrinco(cor_bico="amarelo",cor_pelo="preto",nro_patas=2)
print(ornt)
"""
class Estudante:
    escola='DIO'

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
   
    def __str__(self):
        return f'{self.nome} - {self.numero} - {self.escola}'

def mostrar_valores(*objs):
   for obj in objs:
       print(obj)


nome = input('nome ')
numero = input('numero ')
gui = Estudante(nome,numero)

mostrar_valores(gui)
print('')
"""
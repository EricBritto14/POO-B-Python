class Conta:

    #Criando o construtor em Python
    #Self seria padrão para sempre criar os construtores e depois chamar os atributos
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
        #Se quiser deixar os atributos private, tem que colocar __ antes do nome da variavel, por exemplo o 
        #__limite e __saldo, se não colocar 2 __ atrás ele fica como public
        #Ao ficar privado, só é possível acessa-lo atráves de metodos da mesma classe
    
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque): #__ no nome do metodo para deixar o metodo private e só dar para mexer nele dentro da classe, não chamar fora como metodo comum ou atributo publico
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel_saque #Retornará true se for verdadeiro, e fará o outro metodo, caso caia falso irá para o else do if do metodo de baixo

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite da sua conta. ".format(valor))

    def extrato(self):
        print("Saldo {} do titular: {}".format(self.__saldo, self.__titular))
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #Getters apenas para pegar os valores de alguma variavel que precisa buscar
    @property
    def saldo(self): 
        return self.__saldo
 
    @property
    def titular(self):
        return self.__titular

    @property #Propriedade para quando chamar o metodo nome, não precisar colocar os ()... assim ficaria cliente.nome, como se estivesse mexendo apenas no atributo não no metodo
    #Para funcionar, de padrão o atributo deve estar privado, se não da erro
    #Getter, mas com a função property não precisa por o nome get antes, assim quando chamar parece um metodo normal
    def limite(self):
        return self.__limite

    #Setters para setar e alterar um valor, não tem retorno nos setters, apenas alteração
    @limite.setter #Proprieda de para declarar um setter de uma determinada variável, para quando chamar também só coloque cliente.nome e o novo nome...
    def limite(self, limite):
        self.__limite = limite

    #Estes métodos estáticos, você consegue chamar eles mesmo não criando um objeto conta, não é padrão, mas esses no caso dá
    @staticmethod #@ para colcoar o método como estático a partir de agora
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"Nubank:":"039", "BB":"001", "Itau":"237"}
    
    #Um método estático é adequado para realizar cálculos que não dependem do estado de um objeto específico.
    #Ou fazerem retornos fixos, como  o número de indentidade dos bancos 
    

         
        
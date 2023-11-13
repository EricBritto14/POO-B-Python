class Cliente:

    def __init__(self, nome):
        self.__nome = nome

 
    @property #Propriedade para quando chamar o metodo nome, não precisar colocar os ()... assim ficaria cliente.nome, como se estivesse mexendo apenas no atributo não no metodo
    #Para funcionar, de padrão o atributo deve estar privado, se não da erro
    #Getter, mas com a função property não precisa por o nome get antes, assim quando chamar parece um metodo normal
    def nome(self):
        print("Chamando @property nome()")
        self.__nome.title()

    @nome.setter #Proprieda de para declarar um setter de uma determinada variável, para quando chamar também só coloque cliente.nome e o novo nome...
    def nome(self, nome):
        print("Chamando o setter nome()")
        self.__nome = nome
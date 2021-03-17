class User:
    def __init__(self,codigo,nome,idade,sexo):
        sefl._codigo = codigo
        self._nome = nome
        self._idade = idade
        self._sexo = sexo

#Region Property
@property
def Codigo(self):
    return self._codigo

@Codigo.setter
def Codigo(self,value):
    self._codigo = value


@property
def Nome(self):
    return self._nome

@Nome.setter
def Nome(self,value):
    self._nome = value
    

@property
def Idade(self):
    return self._idade

@Idade.setter
def Idade(self,value):
    self._idade = value
    
    
@property
def Sexo(self):
    return self._sexo

@Sexo.setter
def Sexo(self,value):
    self._sexo = value

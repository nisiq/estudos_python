Python OOP

*Classes*:
  Utilizadas para criar objetos (instancias)
  Classes são utilizadas para AGRUPAR DADOS E FUNÇÕES, podendo reutilizar
  
*Objetos* = são partes dentro de uma class (instancias)
  
  Class = Frutas
  Objects: Maça, Mamão, Banana...
  
 *Construtor* = inicializam campos internos da classe e aloca recursos que um objeto da classe possa demandar
 
"__init__ = método que define o construtor da classe, onde definimos como uma "nova pessoa" será criada.
"self" = sempre o primeiro parâmetro de todos os métodos chamados por uma instância
  
  
#1classe:
class Funcionarios:
    pass

#2objeto:
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#3parametros:
usuario1.nome = 'Nicole'
usuario1.sobrenome = 'Siqueira'
usuario1.data_nasc = '12/12/12'

#4maisparametros:
usuario2.nome = 'Rosana'
usuario2.sobrenome = 'Silva'
usuario2.data_nasc = '10/10/10'
------------------------------------------------------------
#CONSTRUTORES: não precisar passar argumentos da forma acima

class Funcionarios:
#SELF = objeto.argumento
                        #argumentos(self,.....)
    def __init__(self, nome, sobrenome, data_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        
usuario1 = Funcionarios('Nicole', 'Siqueira', '12/12/12')
usuario2 = Funcionarios('Rosana', 'Silva', '10/10/10')
        #não preciso mais das 6 linhas de parametros
        
print(usuario1.nome)
print(usuario2.nome)

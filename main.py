from abc import ABC, abstractmethod
from datetime import date
from datetime import datetime #importando a biblioteca necessária
#import abstractmethod

#lista de livros da biblioteca
listaLivros = []

#Lista dos Funcionarios
listaFuncionarios = []

#Lista dos Usuarios
listaUsuario = []

#Lista de Emprestimos
listaEmprestimo = []

#Classe Livro
class Livro(): 

  def __init__(self, titulo ='', autor = '', anoLancamento='', id=0, nacionalidade='', numPaginas=0, genero='', edicao=''):
    self.titulo = titulo
    self.autor = autor
    self.anoLancamento = anoLancamento
    self.id = id
    self.nacionalidade = nacionalidade
    self.numPaginas = numPaginas
    self.genero = genero
    self.edicao = edicao
  
  #Função CadastrarLivro (método)
  def CadastrarLivro(self):
    self.titulo = input('\nDigite o título: ')
    self.autor = input('Digite o nome do autor: ')
    self.anoLancamento = input('Digite o ano de lançamento: ')
    self.id = input('Digite o código do livro: ')
    self.nacionalidade = input('Digite nacionalidade do livro: ')
    self.numPaginas = input('Digite o número de páginas do livro: ')
    self.genero = input('Digite o gênero do livro: ')
    self.edicao = input('Digite a edição do livro: ')

#Classe Estoque
class Estoque(Livro):
  def __init__(self, titulo ='', autor = '', anoLancamento='', id=0, nacionalidade='', numPaginas=0, genero='', edicao=''):
    super().__init__(titulo, autor, anoLancamento, id, nacionalidade, numPaginas, genero, edicao)

    #função consulta pelo gênero 
    def consultaGenero():   
      genero = input('Digite o gênero do livro: ')

      for i in listaLivros:
        if (i['genero'] == genero):
          print(f"Titulo = {i['titulo']}\nautor = {i['autor']}\nAno de lançamento = {i['anoLancamento']}\nNacionalidade = {i['nacionalidade']}\nNúmero de páginas = {i['numPaginas']}\nGênero = {i['genero']}\nEdição = {i['edicao']}\n")
        else:
          print('Livro não encontrado')

    #função consulta pelo título       
    def consultaTitulo():
      titulo = input('Digite o titulo do livro: ')
      for i in listaLivros:
        if (i['titulo'] == titulo):
          print(f"Titulo = {i['titulo']}\nautor = {i['autor']}\nAno de lançamento = {i['anoLancamento']}\nNacionalidade = {i['nacionalidade']}\nNúmero de páginas = {i['numPaginas']}\nGênero = {i['genero']}\nEdição = {i['edicao']}\n")
        else:
          print('Livro não encontrado')

    #função consulta pelo autor 
    def consultaAutor():
      autor = input('Digite o titulo do livro: ')
      for i in listaLivros:
        if (i['autor'] == autor):
          print(f"Titulo = {i['titulo']}\nautor = {i['autor']}\nAno de lançamento = {i['anoLancamento']}\nNacionalidade = {i['nacionalidade']}\nNúmero de páginas = {i['numPaginas']}\nGênero = {i['genero']}\nEdição = {i['edicao']}\n")
        else:
          print('Livro não encontrado')
 
    #remove livro
    def RemoverLivro():
      id = input('Digite o código do livro: ')
      for i in listaLivros:
        if (i['id'] == id):#compara os ids
          listaLivros.remove(i)#remove da lista
          print('\nLivro removido com sucesso\n')
        else:
          print('Erro! Livro não encontrado')

    while True:
      quant_livros = len(listaLivros)
      print(f"\n***Estoque***\n\nQuantidade total de livros no estoque = {quant_livros}")
      op = int(input('\n1 - Consultar por gênero\n2 - Consultar por título\n3 - Consultar por autor\n4 - Remover Livro\n0 - Sair\n'))
     
      if op == 1:
        consultaGenero()

      elif op == 2:
        consultaTitulo()

      elif op == 3:
        consultaAutor()

      elif op == 4:
        RemoverLivro()

      elif op == 0:
        break

      #Opção inválida
      else:
        print('\nOpção inválida!!\nTente novamente.')
        

class Pessoa():
  @abstractmethod
  def __init__(self, nome="", telefone="", cpf=""):
    self.nome = nome
    self.__telefone = telefone 
    self.cpf = cpf
  
  #método Imprime nome
  def ImprimeNome(self):
    print(f'\n{self.nome} foi cadastrado(a) com sucesso!!!')

#classe funcionario
class CadastrarFuncionario(Pessoa):
  def __init__(self, nome="", telefone=0, cpf="", cargo="", salario=0):
    super().__init__(nome, telefone, cpf)
    self.cargo = cargo
    self.__salario = salario 

  # função cadastrar funcionario    
  def CadastrarFuncionario(self):
    self.nome = input('Digite o nome do funcionário: ')
    self.__telefone = input('Digite o telefone: ')
    self.cpf = input('Digite o cpf: ')
    self.cargo = input('Digite o cargo: ')
    self.__salario = input('Digite o salario: ')
    self.ImprimeNome()

#Função Funcionário
def Funcionario():
  #função remove funcionário
  def RemoverFuncionario():
    cpf = input('Digite o cpf do funcionário: ')
      
    for i in listaFuncionarios:
      if i['cpf'] == cpf:
        listaFuncionarios.remove(i)
        print('\nFuncionário removido com sucesso\n')
      else:
        print('\nErro! Funcionário não encontrado\n')

  #função imprime funcionário 
  def ImprimirFuncionario():
      cpf = input('Digite o cpf do funcionário: ')
    
      for i in listaFuncionarios: 
        if i['cpf'] == cpf:                            
          print(f"Nome: {i['nome']}\nTelefone: {i['_Pessoa__telefone']}\nCPF: {i['cpf']}\nCargo: {i['cargo']}\nSalario: {i['_CadastrarFuncionario__salario']}\n")
        else:
          print('\nErro! Funcionário não encontrado\n')
  
  while True:
    print(f"\n***Funcionário***\n")
    op = int(input('\n1 - Imprimir funcionário\n2 - Remover funcionário\n0 - Sair\n'))

    if op == 1:
      ImprimirFuncionario()

    elif op == 2:
      RemoverFuncionario()
      
    elif op == 0:
        break

    #Opção inválida
    else:
        print('\nOpção inválida!!\nTente novamente.')
    
#classe usuario
class Usuario(Pessoa):
  def __init__(self, nome="", telefone=0, cpf="", status=True):
    super().__init__(nome, telefone, cpf)
    self.status = status
    
  #função cadastrar usuario
  def CadastrarUsuario(self):
    self.nome = input('Digite o nome do usuario: ')
    self.__telefone = input('Digite o telefone: ')
    self.cpf = input('Digite o cpf: ')
    self.ImprimeNome()

#Função Status
def Status():
  cpf = input('Digite o cpf: ')
  
  for i in listaUsuario:
    if i['cpf'] == cpf:
      if i['status'] == True:
        print('Status regular')
      else:
        print('Status irregular')
    else:
      print("Não encontrou o usuário")
      
#Criando uma classe herdeira da classe mãe Livro
class Emprestimo(Livro):
  def __init__(self, titulo ='', autor = '', anoLancamento='', id=0, nacionalidade='', numPaginas=0, genero='',   edicao='', dataEmp='', dataDev='', dataEst='', situacao=True, multa = 0):
    super().__init__(titulo, autor, anoLancamento, id, nacionalidade, numPaginas, genero, edicao)
    self.dataEmp = dataEmp
    self.dataDev = dataDev
    self.dataEst = dataEst
    self.situacao = situacao
    self.multa = multa

  #método cadastrar emprestimo 
  def CadastrarEmprestimo(self):
    self.id = input("Digite o id do emprestimo: ")
    self.dataEmp = (input('Digite a data de empréstimo do livro no formato "DD/MM/AAAA"')) #o funcionario registra a data de emprestimo
    print("\nEmprestimo cadastrado\n")

#Função departamento emprestimo
def DepartamentoEmprestimo():  #função criada para atualizar (definir data de devolucao) e consultar situacao de emprestimo de livro    
  #função atualiza emprestimo
  def AtualizarEmprestimo():
    id = input("Digite o id do emprestimo: ")

    for i in listaEmprestimo:
      if i['id'] == id:
        i['dataDev'] = input('Digite a data de devolução do livro no formato "DD/MM/AAAA"')
        ajusteData(i)
        print("\nEmprestimo atualizado\n")
      else:
        print("Não foi encontrado")
        
  def ajusteData(i): #fç para modificar as datas informadas (string -> datetime) #assim consigo manipular as datas
    #self.dataEmp #visualizando o método de data de empréstimo

    data_int = datetime.strptime(i['dataEmp'], "%d/%m/%Y") #modificando o formato da data de emprestimo para manipulação
    data_int_dev = datetime.strptime(i['dataDev'], "%d/%m/%Y") #modificando o formato da data de devolucao para manipulação
    
    i['dataDev'] = data_int_dev #atribuindo a data de emprestimo com o novo tipo para o atributo dataDev
    print(type(i['dataDev'])) #exibe a classe da dataDev para checar formato
    
    #print(format(data_int, "%d/%m/%Y")) #exibindo a data de emprestimo em formato "27/08/2021"
    #print(type(data_int)) #confere e exibe a classe do objeto "<class 'datetime.datetime'>"
    dataEst = datetime.fromordinal(data_int.toordinal()+7) #faz o cálculo da data estimada: data de empréstimo + 7 dias
    i['dataEst'] = dataEst #atribuindo a data de devolucao com o novo tipo para o atributo dataDev
    
    print(i['dataEst'])
    print(type(i['dataEst']))

  # Função situação 
  def Situacao(): #aqui estou tentando definir a situação e calcular a multa
    id = input("Digite o id do emprestimo: ")

    for i in listaEmprestimo:
      if i['id'] == id:
        dias = (i['dataDev'] - i['dataEst']).days
        if dias <= 0:
          i['multa'] = 0
          i['situacao'] = True #a situação prevista inicial é que o livro foi entregue no prazo
          print("Livro entregue no prazo")
        else:
          i['multa'] += (2*dias)
          i['situacao'] = False
          print("O livro não foi entregue no prazo.")
          print(f"O livro foi devolvido com {dias} dias de atraso")
          print(f"O valor da multa é de: {i['multa']} reais")
      else:
        print("Não foi encontrado")

  while True:
    print(f"\n***Emprestimo***\n")
    op = int(input('\n1 - Cadastrar empréstimo\n2 - Atualizar empréstimo\n3 - Consultar situação de empréstimo\n0 - Sair\n'))
      
    #Cadastrar emprestimo      
    if op == 1:
      emp = Emprestimo()
      emp.CadastrarEmprestimo()
      listaEmprestimo.append(vars(emp)) #add data de emprestimo na lista emprestimo
              
    elif op == 2:
      AtualizarEmprestimo()

    elif op == 3:
      Situacao()

    elif op == 0:
      break

    #Opção inválida
    else:
      print('\nOpção inválida!!\nTente novamente.')

#Menu do programa
while True:
  print('\n*****Sistema da biblioteca*****\n')
  op = int(input('\nEscolha a operação que deseja realizar:\n1 - Cadastrar Livro\n2 - Cadastrar Funcionario\n3 - RH (Funcionário)\n4 - Cadastrar Usuário\n5 - Consultar Estoque\n6 - Empréstimo de livros\n7 - Status do usuário\n0 - Sair\n'))
  
  #Cadastrar Livro
  if op == 1:
      livro = Livro()#cria um livro
      livro.CadastrarLivro()#modifica os atributos do livro
      listaLivros.append(vars(livro))#adiciona na lista de livros

  #Cadastrar os funcionarios
  elif op == 2:
      funcionario = CadastrarFuncionario()
      funcionario.CadastrarFuncionario()
      listaFuncionarios.append(vars(funcionario))

  #RH (Funcionário)
  elif op == 3:
    Funcionario()
     
  #Cadastrar Usuários
  elif op == 4:
      usuario = Usuario()
      usuario.CadastrarUsuario()
      listaUsuario.append(vars(usuario))

  elif op == 5:
    Estoque()

  #Departamento de Emprestimo
  elif op == 6:
    DepartamentoEmprestimo()
    
  #Status  
  elif op == 7:
    Status()

  #sair
  elif op == 0:
      break
  
  #Opção inválida
  else:
    print('\nOpção inválida!!\nTente novamente.')

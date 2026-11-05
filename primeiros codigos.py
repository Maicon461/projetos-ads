import sqlite3
from pathlib import Path   #path é uma biblioteca que ajuda a localizar arquivos no computador de forma correta.

DB_PATH = Path(__file__).with_name("loja_veiculo.db") #criando um arquivo de banco de dados chamado loja_veiculo.db na mesma pasta do script.

#criando uma classe veiculo para representar os veiculos cadastrados no sistema.
class veiculo:
  def __init__(self, marca, modelo, ano, preco): #recebe os atributos do veiculo
      #self...salva os atributos do veiculo para serem usados em outros métodos da classe.
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.preco = preco
#(exibir)imprime os atributos do veiculo de forma formatada, com o preço exibido com duas casas decimais e separador de milhar.
  def exibir(self):
    print(f"{self.marca} {self.modelo} {self.ano} {self.preco:,.2f}")

#funções de conexão e validação de entrada de dados

def conectar_db():
  return sqlite3.connect(DB_PATH)   #conecta ao banco de dados

#funções para ler e validar entradas de dados do usuário, garantindo que sejam do tipo correto (inteiro ou float).
def ler_inteiro(mensagem):
  while True:              #loop infinito para continuar pedindo a entrada até que seja válida
    try:                   #tenta converter a entrada do usuário para inteiro  
      return int(input(mensagem)) #retorna o valor convertido se for válido
    except ValueError:             #captura o erro quando a pessoa digita texto ou outro tipo de dado que não seja inteiro             
      print("Valor invalido. Digite um numero inteiro.")

#faz a mesma coisa que a função ler_inteiro, mas para números de ponto flutuante (float). Substitui vírgulas por pontos para permitir a entrada de números decimais.
def ler_float(mensagem):   
  while True:
    try:
      return float(input(mensagem).replace(",", ".")) #aceita tanto vírgula quanto ponto como separador decimal ex: 1000,50 ou 1000.50
    except ValueError:                                #captura o erro quando a pessoa digita texto ou outro tipo de dado que não seja float
      print("Valor invalido. Digite um numero valido.")


#criando banco de dados(ou lista vazia)
conexao = conectar_db()  #abre a conexão com o banco de dados
cursor = conexao.cursor() #cria um cursor para executar comandos SQL no banco de dados
#cria a tabela veiculos no banco de dados, caso ela não exista. A tabela possui colunas para id, marca, modelo, ano e preco.
cursor.execute("""
  CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT,
    modelo TEXT,
    ano INTEGER,
    preco REAL
  )
""")
conexao.commit() #salva a tabela no banco de dados
conexao.close()  #fecha a conexão com o banco de dados


#função para cadastrar um veiculo novo.(essa função apenas para add veiculo)
def cadastrar_veiculo():
  marca = input("Digite a marca do veiculo: ").strip() #(strip)remove espaços em branco no início e no final da string digitada pelo usuário.
  modelo = input("Digite o modelo do veiculo: ").strip()
#condição para verificar se a marca e o modelo não estão vazios. Se estiverem, exibe uma mensagem de erro e retorna da função sem cadastrar o veículo.
  if not marca or not modelo:
    print("Marca e modelo nao podem ficar vazios.")
    return

  ano = ler_inteiro("Digite o ano do veiculo: ") #usa a função ler_inteiro para garantir que o ano seja um número inteiro válido.
  preco = ler_float("Digite o preco do veiculo: ") #usa a função ler_float para garantir que o preço seja um número de ponto flutuante válido.

  try: #tenta inserir os dados do veículo no banco de dados. Se ocorrer algum erro, captura a exceção e exibe uma mensagem de erro.
    conexao = conectar_db() #conecta ao banco de dados
    cursor = conexao.cursor() #cria um cursor para executar comandos SQL no banco de dados
    cursor.execute(
      "INSERT INTO veiculos (marca, modelo, ano, preco) VALUES (?, ?, ?, ?)", #usa SQL como parametros evitando erro de SQL e deixando mais seguro.
      (marca, modelo, ano, preco) 
    )
    conexao.commit() #salva as alterações no banco de dados
    print("Veiculo cadastrado com sucesso!")
  except sqlite3.Error as erro:              #captura o erro quando ocorre algum problema ao cadastrar o veículo no banco de dados
    print(f"Erro ao cadastrar veiculo: {erro}")
  finally:            #garante que a conexão com o banco de dados seja fechada, mesmo que ocorra um erro durante o cadastro do veículo.
    if 'conexao' in locals():
      conexao.close()


#Proxima função é a de pesquisar veiculo
#detalhe termo_pesquisa(significa que qualquer pedaço da palavra vai se completar)
def pesquisar_veiculo():
  termo_pesquisa = input("Digite o termo de pesquisa: ").strip() #le o termo de pesquisa e remove os espacos em branco com (strip).
#função abaixo verifica se o termo de pesquisa está vazio.se tiver,exibe mensagem de erro e retorna da função sem realizar a pesquisa.
  if not termo_pesquisa:
    print("Digite algo para pesquisar.")
    return

  try: #tenta pesquisar os veículos no banco de dados que correspondam ao termo de pesquisa.se ocorrer erro, captura a exceção e exibe uma mensagem de erro.
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(
      """
        SELECT marca, modelo, ano, preco FROM veiculos 
        WHERE LOWER(marca) LIKE LOWER(?) OR LOWER(modelo) LIKE LOWER(?) 
      """,
      (f"%{termo_pesquisa}%", f"%{termo_pesquisa}%") #faz pesquisa parcial %% like.
    ) #executa a consulta SQL e (lower)converte para minuscula(like)busca qualquer parte da palvra.

    linhas_encontradas = cursor.fetchall() #pega todas as linhas encontradas na pesquisa e armazena na variável linhas_encontradas.

    if not linhas_encontradas:
      print("Nenhum veiculo encontrado.") #se nada for encontrado, exibe mensagem de erro e retorna da função sem exibir nenhum veículo.
      return

    print("Veiculos encontrados:")
    for linha in linhas_encontradas: #percorre cada linha e cria um objeto veiculos com os dados da linha.
      marca_banco, modelo_banco, ano_banco, preco_banco = linha
      carro_encontrado = veiculo(marca_banco, modelo_banco, ano_banco, preco_banco)
      carro_encontrado.exibir() #chama o método exibir do objeto veiculo para imprimir os atributos do veiculo.
  except sqlite3.Error as erro: #trata o erro caso ocorra algum problema ao pesquisar os veículos no banco de dados.
    print(f"Erro ao pesquisar veiculo: {erro}")
  finally:     #garante que a conexão com o banco de dados seja fechada, mesmo que ocorra um erro durante a pesquisa do veículo.
    if 'conexao' in locals():
      conexao.close()


#criando loop de repetição.Impede que o sistema feche depois de terminar o cadastro
#roda enquanto for verdadeira(while true)
while True: #repetição infinita para exibir o menu e permitir que o usuário escolha uma opção até que ele decida sair.
  print("\nMenu:")
  print("1. Cadastrar veiculo")
  print("2. Pesquisar veiculo")
  print("0. Sair")
  opcao = input("Escolha uma opcao: ")
 #abaixo verifica a opção escolhida pelo usuário e chama a função correspondente. Se a opção for inválida, exibe uma mensagem de erro.
  if opcao == "1":
    cadastrar_veiculo()
  elif opcao == "2":
    pesquisar_veiculo()
  elif opcao == "0":
    break
  else:   #significa caso contrario,ou seja, se a opção digitada não for 1,2 ou 0, exibe mensagem de erro.
    print("Opcao invalida.Tente novamente.")

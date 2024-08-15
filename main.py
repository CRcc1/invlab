import math


# Classe para armazenar informações de login
class Login:

  def __init__(self, nome, senha, cpf):
    self.nome = nome
    self.senha = senha
    self.cpf = cpf


# Classe para armazenar informações da carteira de investimento
class CarteiraInvestimento:

  def __init__(self, montante, periodo):
    self.montante = montante
    self.periodo = periodo
    self.investimentos = []  # Lista para armazenar os tipos de investimento

  def cadastrar_investimento(self, tipo, rendimento_anual):
    investimento = {"tipo": tipo, "rendimento_anual": rendimento_anual}
    self.investimentos.append(investimento)

  def listar_investimentos(self):
    for investimento in self.investimentos:
      print(f"Tipo de Investimento: {investimento['tipo']}")
      print(f"Rendimento Anual: {investimento['rendimento_anual']}")

  def calcular_rendimento_total(self):
    rendimento_total = 0.0
    for investimento in self.investimentos:
      rendimento_anual = investimento['rendimento_anual']
      rendimento_total += self.montante * (1 + rendimento_anual)**self.periodo
    return rendimento_total


# Classe Cliente que contém informações de login e carteira de investimento
class Cliente:

  def __init__(self, nome, login, senha, cpf):
    self.login_info = Login(nome, senha, cpf)
    self.carteira_investimento = None

  def cadastrar_carteira(self, montante, periodo):
    self.carteira_investimento = CarteiraInvestimento(montante, periodo)

  def cadastrar_investimento(self, tipo, rendimento_anual):
    if self.carteira_investimento is not None:
      self.carteira_investimento.cadastrar_investimento(tipo, rendimento_anual)


# Método de validação de login
def validar_login(nome, senha, cpf):
  tem_numero = any(c.isdigit() for c in nome)

  tem_letra = True
  tem_numero = False

  for char in senha:
    if char.isalpha():
      tem_letra = True
    elif char.isdigit():
      tem_numero = True

  return  tem_numero and tem_letra


def calcular_rendimento_mensal(rendimento_anual):
  return (1 + rendimento_anual)**(1 / 12) - 1


def calcular_rendimento_mensal_dinheiro(rendimento_mensal, montante_inicial):
  return montante_inicial * rendimento_mensal


clientes = []

for i in range(5):
  num_clientes = 0

  while num_clientes < 2:
    print(f"Cadastro do cliente {i + 1}:")

    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")

    if validar_login(nome, senha, cpf):
      print("Login válido!")
    else:
      print("Login inválido!")
      break

    cliente = Cliente(nome, nome, senha, cpf)

    montante = float(input("Digite o montante a ser aplicado: "))
    periodo = int(input("Digite o período de tempo (em anos) da aplicação: "))

    cliente.cadastrar_carteira(montante, periodo)

    escolha = int(
        input("Escolha o tipo de aplicação:\n"
              "1. Conservadora (11,75% de rendimento anual)\n"
              "2. Arriscada (17% de rendimento anual)\n"
              "3. Mista (15% de rendimento anual)\n"
              "4. ARCA (50% de rendimento anual sem garantia FGC)\n"
              "5. Ações Rendimento, dividendos e cripto (30% de rendimento anual)\n"
              "Opção: "))

    rendimento_anual = 0.0

    if escolha == 1:
      rendimento_anual = 0.1188
    elif escolha == 2:
      rendimento_anual = 0.17
    elif escolha == 3:
      rendimento_anual = 0.15
    elif escolha == 4:
      rendimento_anual = 0.50
    elif escolha == 5:
      rendimento_anual = 0.30
    else:
      print("Opção inválida.")
      continue

    rendimento_mensal = calcular_rendimento_mensal(rendimento_anual)
    rendimento_mensal_dinheiro = calcular_rendimento_mensal_dinheiro(
        rendimento_mensal, montante)

    montante_final = montante * (1 + rendimento_anual)**periodo

    print(f"Simulação do cliente {i + 1}:")
    print(f"Nome: {cliente.login_info.nome}")
    print(f"Montante inicial: R${montante:.2f}")
    print(f"Rendimento mensal: R${rendimento_mensal_dinheiro:.2f}")
    print(f"Montante final após {periodo} anos: R${montante_final:.2f}\n")

    cliente.cadastrar_investimento("Investimento Escolhido", rendimento_anual)

    num_clientes += 1

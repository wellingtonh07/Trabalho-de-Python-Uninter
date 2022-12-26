listapecas = []
#---------------COMEÇO CADASTRO PEÇAS-------------------------
def cadastrarPecas(codigo):
  print('Você selecionou a opção de Cadastrar Peça ')
  print('O código do produto a ser cadastrado é: 00{}' . format(codigo))
  nome = input('Por favor, entre com o NOME da peça: ')
  fabricante = input('Por favor, entre com o FABRICANTE da peça: ')
  preco = input('Por favor, entre com o VALOR(R$) da peça: ')
  dicionarioPecas ={'codigo': codigo,
                    'nome': nome,
                    'fabricante': fabricante,
                    'preco': preco}
  listapecas.append(dicionarioPecas.copy())

#---------------FIM CADASTRO PEÇAS----------------------------

#---------------COMEÇO CONSULTA PEÇAS-------------------------
def consultaPecas():
  while True:
    try:
      print('Você selecionou a opção de Consultar Peças ')
      opcaoconsultar = int(input('Digite a Opção Desejada:\n'
                            '1-Consultar Todas as Peças \n'
                            '2-Consultar Peças por código \n'
                            '3-Consultar Peças por fabricante \n'
                            '4-Retornar'
                            '\n>>'))
      if opcaoconsultar == 1:
        for pecas in listapecas:
          for key, value in pecas.items():
            print('{} : {} \n' . format(key,value))
      elif opcaoconsultar ==2:
        entrada = int(input('Digite o CÓDIGO desejado: '))
        for pecas in listapecas:
          if( pecas['codigo']==entrada):
            for key, value in pecas.items():
              print('{} : {} \n'.format(key, value))
      elif opcaoconsultar == 3:
        entrada = input('Digite o FABRICANTE da peça: ')
        for pecas in listapecas:
            if (pecas['fabricante'] == entrada):
                for key, value in pecas.items():
                    print('{} : {} \n'.format(key, value))
      elif opcaoconsultar == 4:
        break
      else:
        print('Opção Inválida. Tente Novamente')
        continue
    except ValueError:
      print('Valores não Inteiros')


#---------------FIM CONSULTA PEÇAS----------------------------
# ---------------COMEÇO REMOVER PEÇAS-------------------------
def removerPecas():
  print('Você selecionou a opção de Remover Peça')
  entrada = int(input('Digite o código da peça que deseja Remover: '))
  for pecas in listapecas:
    if (pecas['codigo'] == entrada):
       listapecas.remove(pecas)

# ---------------FIM REMOVER PEÇAS----------------------------
# ---------------COMEÇO MAIN----------------------------------

print('Bem Vindo ao Controle de Estoque da Bicicletaria do Wellington de Holanda Nascimento')
registroproduto = 0
while True:
  try:
    opcao = int(input('Escolha a opção desejada:\n'
                     '1-Cadastrar Peças \n'
                     '2-Consultar Peças \n'
                     '3-Remover Peças \n'
                     '4-Sair'
                     '\n>>'))
    if opcao == 1:
      registroproduto = registroproduto + 1
      cadastrarPecas(registroproduto)
    elif opcao == 2:
      consultaPecas()
    elif opcao == 3:
      removerPecas()
    elif opcao == 4:
      print('Programa Finalizado')
      break
    else:
          print('Opção Inválida. Tente Novamente')
          continue
  except ValueError:
    print('Valores não Inteiros, digite novamente')
# ---------------FIM MAIN----------------------------
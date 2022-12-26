print('Bem vindo a lanchonete do Wellington de Holanda Nascimento')
print('*' * 15 , 'Cardapio' , '*' * 15)
print("""| Codigo |     Descrição      | Valor |
| 100 |   Cachorro quente     |  9,00 |
| 101 | Cachorro quente duplo | 11,00 |
| 102 |     X-Egg             | 12,00 |
| 103 |     X-Salada          | 12,00 |
| 104 |     X-Bacon           | 14,00 |
| 105 |     X-Tudo            | 17,00 |
| 200 |   Refrigerante Lata   |  5,00 |
| 201 |     Chá Gelado        |  4,00 |""")
total = 0
while True:
  codigo = int(input('Entre com o codigo desejado: '))
  if codigo == 100:
    valor = 9
    total = total + valor
    print('Você escolheu o Cachorro Quente de 9,00 reais')

  elif codigo == 101:
    valor = 11
    total = total + valor
    print('Você escolheu o Cachorro Quente duplo de 11,00 reais.')

  elif codigo == 102:
    valor = 12
    total = total + valor
    print('Você escolheu o X-Egg de 12,00 reais')

  elif codigo == 103: 
    valor = 12
    total = total + valor
    print('Você escolheu o X-Salada de 12,00 reais')
    
  elif codigo == 104:
    valor = 14
    total = total + valor
    print('Você escolheu o X-Bacon de 14,00 reais')

  elif codigo == 105:
    valor = 17
    total = total + valor
    print('Você escolheu o X-Tudo de 17,00 reais')

  elif codigo == 200:
    valor = 5
    total = total + valor
    print('Você escolheu o Refrigerante Lata de 5,00 reais')

  elif codigo == 201:
    valor = 4
    total = total + valor
    print('Você escolheu o Chá Gelado de 4,00 reais')
        
  else:
    print('Opção Inválida')
    continue
    
  pedir = str(input("""Deseja pedir mais alguma coisa?
  1- sim
  0- não 
  """))

  if pedir == '1':
    continue 
    
  else:
    valor_total = total
    print('O valor que você vai pagar é de {} reais' .format(valor_total))
    break
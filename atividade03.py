print('Bem vindo a companhia de logística de Wellington de Holanda Nascimento')
def dimensoes_Objeto():
  while True:
    try:
      altura = float(input('Digite a altura do objeto(em cm): '))
      comprimento = float(input('Digite o comprimento do objeto(em cm): '))
      largura = float(input('Digite a largura do objeto(em cm: '))
    except ValueError:
      print('Você digitou um valor não numerico')
      print('Por favor, entre com as dimensões desejadas novamente')
      continue
        
      volume = (altura * largura * comprimento)
      print('O volume desse objeto em(cm³) é: {}.' .format(volume))
    
      if volume < 1000:
        valor = 10
        return valor
        break
            
      elif 1000 <= volume < 10000:
        valor = 20 
        return valor
        break
            
      elif 10000 <= volume < 30000:
        valor = 30
        return valor
        break
            
      elif 30000 <= volume < 100000:
        valor = 50
        return valor
        break
      
      else:
        print('Não aceitamos objetos com dimensões tão grandes.')
        print('Por favor, entre com as dimensões desejadas novamente.')
        continue
                        
            
                
def peso_Objeto():
  while True:
    try:
      peso = float(input('Qual o peso do objeto(em kg)? '))
        
    except ValueError:
      print('Voce digitou peso do objeto com valor não numérico')
      print('Por favor, entre com o peso desejado novamente')
      continue
        
    if peso <= 0.1:
      multiplicador = 1
      return multiplicador
      break
        
    elif 0.1 < peso <= 1:
      multiplicador = 1.5
      return multiplicador
      break
            
    elif 1 < peso <= 10:
      multiplicador = 2
      return multiplicador
      break
            
    elif 10 < peso <= 30:
      multiplicador = 3
      return multiplicador
      break
            
    else:
      print('Não aceitamos objetos tão pesados.')
      continue
            

def rota_Objeto():
  while True:
    rota = str(input('''Por favor, selecione a rota:
    RS - De Rio de Janeiro até São Paulo
    SR - De São Paulo até o Rio de Janeiro
    BS - De Brasília até São Paulo
    SB - De São Paulo até Brasília
    BR - De Brasília até Rio de Janeiro
    RB - De Rio de Janeiro até Brasília
    '''))
            	
        	
    if rota == 'RS':
      multiplicador = 1
      return multiplicador
      break
            
    elif rota == 'SR':
      multiplicador = 1
      return multiplicador
      break
            
    elif rota == 'BS':
      multiplicador = 1.2
      return multiplicador
      break
            
    elif rota == 'SB':
      multiplicador = 1.2
      return multiplicador
      break
            
    elif rota == 'BR':
      multiplicador = 1.5
      return multiplicador
      break
            
    elif rota == 'RB':
      multiplicador = 1.5
      return multiplicador
      break

    else:
      print('Você digitou uma rota que não existe')
      print('Por favor, entre com a rota desejada novamente')
      continue	
            
                         


dimensao = dimensoes_Objeto()
peso = peso_Objeto()
rota = rota_Objeto()
total = dimensao * peso * rota

print('O valor que voce vai pagar é {} (Dimensões: {} * peso {} * rota {})'  .format(total, dimensao, peso, rota))
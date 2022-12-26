print('Bem vindo a loja do Wellington de Holanda Nascimento ')
vp = float(input('Entre com o valor do produto: '))
vq = float(input('Entre com o valor de quantidade: '))
vtsd = vp * vq

if vq <= 9:
   print('O valor total sem desconto é {} reais.' .format(vtsd))

elif 10 <= vq <= 99:
   vtcd = vtsd - (vtsd * 5 / 100)
   print('O valor total sem desconto é {:.2f} reais ' .format(vtsd))
   print('O valor total com desconto é de {:.2f} reais. (desconto 5%)' .format(vtcd))

elif 100 <= vq <= 999:
   vtcd = vtsd - (vtsd * 10 / 100)
   print('O valor total sem desconto é {:.2f} reais.' .format(vtsd))
   print('O valor total com desconto é {:.2f} reais. (desconto 10%)' .format(vtcd))

elif vq >= 1000:
   vtcd = vtsd - (vtsd * 15 / 100)
   print('O valor total sem desconto foi {:.2f} reais.' .format(vtsd))
   print('O valor total com desconto foi {:.2f} reais. (desconto 15%)' .format(vtcd))
   
else:
   print('Programa encerrado. Tenha um bom dia')

#Coloquei as variáveis assim, com poucas letras porque acho que deixou o código mais objetivo.
#Abaixo está o significado dessas variaveis:
#vp = valor do produto
#vq = valor da quantidade
#vtsd = valor total sem desconto
#vtcd = valor total com desconto
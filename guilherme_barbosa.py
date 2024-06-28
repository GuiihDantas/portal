#Importando Biblioteca Requests
import requests

# Setando variável para consultar a página 
money = requests.get('https://dolarhoje.com.br')

# Printando na tela o status da página
# print(money.status_code)

# Pegando o conteúdo da página 
money_text = money.text

# Verificando a posição do str US$ -> 3876
money_uss = money_text.find("US$")   


# Posição "hoje" -> 3941
money_day = money_text.index('hoje', 3876)

# Coletando o trecho entre as duas variáveis
trecho = money_text[money_uss:money_day]

# Substituindo , por . do Dolar
valor_dolar = trecho[4:8]
vl_dol_float = round(float(valor_dolar.replace(',', '.')),2)

# Substituindo , por . do Real
valor_real = trecho[42:46]
vl_real_float = round(float(valor_real.replace(',', '.')),2)
#vl_real_float

# Setando variável para consultar a página 
bit_real = requests.get('https://dolarhoje.com/bitcoin-hoje/')

# Printando na tela o status da página
# print(bit_real.status_code)

# Pegando o conteúdo da página 
bit_real_text = bit_real.text

# Verificando a posição do str ฿ -> 34390
bit_real_uss = bit_real_text.find("฿") 

# Posição "hoje" -> 34636
bit_real_day = bit_real_text.index('hoje', 34390)

# Coletando o trecho entre as duas variáveis
trecho_bit_real = bit_real_text[bit_real_uss:bit_real_day]

# Substituindo , por . do bit_real
valor_bit_real = bit_real_text[34593:34602]
vl_bit_real_float = round(float(valor_bit_real.replace(',', '.')),2)

# Setando variável para consultar a página 
bit = requests.get('https://crypto.com/price/pt-BR/bitcoin')
# Printando na tela o status da página
#print(bit.status_code)

# Pegando o conteúdo da página 
bit_text = bit.text

# Verificando a posição do str US$ -> 51550
bit_uss = bit_text.find("Volume de 24H") 
#bit_uss

# Posição "hoje" -> 174772
bit_day = bit_text.index('Dominância', 51550)
#bit_day

# Coletando o trecho_bit entre as duas variáveis
trecho_bit = bit_text[bit_uss:bit_day]

# Substituindo , por . do bit
valor_bit = trecho_bit[97:102]
vl_bit_float = round(float(valor_bit.replace(',', '.')),2)

# Imprimindo Resultados
print(f'Guilherme_Dantas >> 1 bitcoin vale R${vl_bit_real_float:.2f} Mil Reais'f' e vale US${vl_bit_float:.3f}'f' Mil Dólares (1 Dólar vale R${vl_real_float:.2f} Reais)')





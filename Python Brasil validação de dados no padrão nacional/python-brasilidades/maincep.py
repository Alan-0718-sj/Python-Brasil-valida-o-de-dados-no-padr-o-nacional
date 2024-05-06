# import requests
from acesso_cep import BuscaEndereco
cep = "01001000"
objeto_cep = BuscaEndereco(cep)

# print(objeto_cep)
# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(type(r.text))
# print(type(a))
# print(dir(a))

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

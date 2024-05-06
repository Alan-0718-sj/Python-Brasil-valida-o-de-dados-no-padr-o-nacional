from datetime import datetime, timedelta
from datas_br import DatasBr


hoje = DatasBr()
print(hoje.tempo_cadastro())



# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1,hours=20)
# print(amanha - hoje)



# cadastro = DatasBr()
# print(cadastro)

'''
hoje = datetime.today()
hoje_formtada = hoje.strftime("%d/%m/%Y - %H:%M")
print(hoje)
print(hoje_formtada)
print(type(hoje_formtada))
'''





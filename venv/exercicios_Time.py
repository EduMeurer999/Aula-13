import time
from datetime import datetime

agora  = datetime.now().date().strftime('%d-%m-%Y')
agora = datetime.strptime(agora, '%d-%m-%Y')
fim=datetime.strptime("21-12-2018", "%d-%m-%Y")
inicio = datetime.strptime("19-01-2018", '%d-%m-%Y')
qtd_dias = abs((fim - inicio).days)
print("Total de dias letivos: ",qtd_dias)
print("Faltam ",abs((fim-agora).days)," dias p/ acabar o ano letivo")
data = input("\nInforme uma data no formato: dd-mm-aaaa: ")
dateData = datetime.strptime(data, "%d-%m-%Y")
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
meses = ('','Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
print(dias[dateData.weekday()])
print(meses[dateData.month])
print(abs((agora.year-dateData.year)), " Anos")



#tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec
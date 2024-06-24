#%%
from pytrends.request import TrendReq

# Configuração para o Brasil e em português
pytrends = TrendReq(hl='pt-BR', tz=180)

# Defina os termos de pesquisa em português
kw_list = ["token", "Inteligência Artificial", "Jogo do Tigrinho"]

# Coleta de dados de tendência para os últimos 12 meses no Brasil
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='BR', gprop='')

# Recuperação dos dados
data = pytrends.interest_over_time()
print(data)

#%%
data.to_excel("googletrends.xlsx")
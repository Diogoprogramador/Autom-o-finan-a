import pandas as pd
import yfinance as yf

# Ler o arquivo carteira.txt
with open("carteira.txt", "r") as arquivo:
    texto = arquivo.readlines()

# Processar os dados da carteira
carteira = {}
for linha in texto:
    try:
        ticker, valor = linha.split("-")
        ticker = f"{ticker.strip()}.SA"
        valor = float(valor.strip())
        carteira[ticker] = valor
    except ValueError:
        print(f"Erro ao processar a linha: {linha.strip()}")

# Exibir a carteira processada
print("Carteira:", carteira)

# Configurar os ativos e datas para análise
ativos = list(carteira.keys())
ativos.append("^BVSP")
data_inicial = "2024-01-01"
data_final = "2024-12-18"

# Obter cotações ajustadas usando yfinance diretamente
try:
    tabela_cotacoes = yf.download(ativos, start=data_inicial, end=data_final)
    if "Adj Close" in tabela_cotacoes:
        tabela_cotacoes = tabela_cotacoes["Adj Close"]
    else:
        print("Dados de 'Adj Close' não disponíveis. Usando 'Close' em vez disso.")
        tabela_cotacoes = tabela_cotacoes["Close"]
    print(tabela_cotacoes.head())  # Visualizar as primeiras linhas da tabela
except Exception as e:
    print("Erro ao obter dados de cotações:", e)
    exit()

# Calcular rentabilidades
rentabilidades = {}
for ativo in tabela_cotacoes.columns:
    try:
        rentabilidade = tabela_cotacoes[ativo][-1] / tabela_cotacoes[ativo][0]
        rentabilidades[ativo] = rentabilidade
    except Exception as e:
        print(f"Erro ao calcular rentabilidade para {ativo}: {e}")
print("Rentabilidades:", rentabilidades)

# Calcular o valor inicial e final da carteira
valor_inicial = sum(carteira.values())
valor_final = sum(carteira[ativo] * rentabilidades[ativo] for ativo in carteira if ativo in rentabilidades)
rentabilidade_carteira = (valor_final / valor_inicial) - 1

# Exibir os resultados
print(f"Valor inicial da carteira: R${valor_inicial:.2f}")
print(f"Valor final da carteira: R${valor_final:.2f}")
print(f"Rentabilidade da carteira: {rentabilidade_carteira:.1%}")

# Comparar com a rentabilidade do índice
if "^BVSP" in rentabilidades:
    rentabilidade_indice = rentabilidades["^BVSP"] - 1
    print(f"Rentabilidade do índice Bovespa (^BVSP): {rentabilidade_indice:.1%}")
else:
    print("Não foi possível calcular a rentabilidade do índice Bovespa.")

Automação de Finanças com Pandas e yFinance
Descrição
Este projeto utiliza as bibliotecas Pandas e yFinance para automatizar a coleta e análise de dados financeiros. O yFinance permite acessar informações de mercado, como cotações de ações, históricos de preços e outros dados financeiros, enquanto o Pandas é usado para manipulação e análise desses dados.

Pré-requisitos
Antes de rodar o projeto, instale as dependências necessárias utilizando o seguinte comando:

bash
Copiar código
pip install pandas yfinance
Bibliotecas Utilizadas
Pandas (import pandas as pd): Usado para manipulação e análise de dados. O Pandas fornece estruturas de dados eficientes para armazenar e trabalhar com dados financeiros.

yFinance (import yfinance as yf): Biblioteca para baixar dados financeiros históricos e em tempo real de ações, índices, ETFs, entre outros, diretamente do Yahoo Finance.

Como Usar
1. Baixar Dados Financeiros
Utilize o yFinance para obter dados financeiros de ações, ETFs ou índices. Por exemplo, para baixar dados históricos de uma ação, use o código abaixo:

python
Copiar código
import yfinance as yf
import pandas as pd

# Defina o ticker da ação
ticker = 'AAPL'

# Baixe os dados históricos para os últimos 5 anos
dados = yf.download(ticker, start='2018-01-01', end='2023-01-01')

# Exibir as primeiras linhas dos dados
print(dados.head())
Este exemplo baixa os dados históricos da ação da Apple (AAPL) para o período de 1º de janeiro de 2018 até 1º de janeiro de 2023.

2. Analisar os Dados
Você pode usar o Pandas para realizar análises, como calcular médias móveis, retornos diários ou outras métricas financeiras. Exemplo:

python
Copiar código
# Calcular a média móvel de 50 dias
dados['SMA50'] = dados['Close'].rolling(window=50).mean()

# Calcular o retorno diário
dados['Retorno'] = dados['Close'].pct_change()

# Exibir as primeiras linhas com as novas colunas
print(dados[['Close', 'SMA50', 'Retorno']].head())
3. Automatizar a Coleta de Dados
Este projeto pode ser estendido para automatizar a coleta de dados financeiros de múltiplos ativos. Você pode configurar um script para obter dados financeiros de diferentes ações, ETFs ou índices em tempo real e salvar os dados para análises posteriores.

Exemplo para baixar dados de múltiplos tickers:

python
Copiar código
tickers = ['AAPL', 'GOOGL', 'MSFT']

# Baixar dados de múltiplos tickers
dados_completos = yf.download(tickers, start='2020-01-01', end='2023-01-01')

# Exibir os dados para o primeiro ticker
print(dados_completos['Adj Close']['AAPL'].head())
4. Salvar os Dados
Você pode salvar os dados em arquivos CSV ou Excel para posterior análise ou visualização.

python
Copiar código
# Salvar os dados em um arquivo CSV
dados.to_csv('dados_acao.csv')

# Salvar os dados em um arquivo Excel
dados.to_excel('dados_acao.xlsx')
Exemplo Completo de Automação
Aqui está um exemplo completo que baixa dados financeiros de uma ação, calcula algumas métricas e salva os resultados em um arquivo CSV:

python
Copiar código
import yfinance as yf
import pandas as pd

# Defina o ticker da ação
ticker = 'AAPL'

# Baixe os dados históricos
dados = yf.download(ticker, start='2018-01-01', end='2023-01-01')

# Calcular a média móvel de 50 dias
dados['SMA50'] = dados['Close'].rolling(window=50).mean()

# Calcular o retorno diário
dados['Retorno'] = dados['Close'].pct_change()

# Salvar os dados em um arquivo CSV
dados.to_csv(f'{ticker}_dados.csv')

print(f"Dados de {ticker} salvos com sucesso!")
Contribuições
Contribuições são bem-vindas! Para contribuir, siga as etapas abaixo:

Fork o repositório.
Crie uma nova branch para a sua funcionalidade (git checkout -b feature-nome).
Realize suas alterações.
Commit suas mudanças (git commit -m 'Adicionando nova funcionalidade').
Envie suas alterações para o repositório original (git push origin feature-nome).
Abra um Pull Request.

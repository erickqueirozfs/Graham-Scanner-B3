import re
from datetime import datetime, timedelta

import requests
import yfinance as yf


def validar_codigo(ativo):
    """
    Analisa se o ativo é brasileiro ou não. O padrão para ações brasileiras costumam ter 4 letras e um número inteiro no final, sendo 3 ou 4.

    Args:
        ativo (str): Ticker do ativo, ex.:'BBAS3','VALE3','GOAU4'.

    Returns:
        bool: Irá retornar True se for um ativo brasileiro.

    Exemplos:
        >>> validar_codigo("bbas3")
        True
    """
    padrao = r"^[A-Za-z]{4}[34]$"
    return bool(re.fullmatch(padrao, ativo))


def buscar_indicadores(ticker_name: str) -> dict:
    """
    Pegar dados das ações.

    Args:
        ticker_name (str):Ticker do ativo

    Returns:
        dict: Retorna dados sobre o ativo

    Exemplos:
        >>> buscar_indicadores("BBAS3")
        {
        'Ticker': 'BBAS3.SA',
        'CotacaoAtual': 25.43,
        'LPA (Lucro por Acao)': 2.4,
        'VPA (Valor Patrimonial por Acao)': 32.427,
        'P/VP': 0.7842231,
        'ROE': 0.08884,
        'DY (Dividend Yield)': 0.72
        }
    """

    def calcular_dy_real():
        """
        Pegar porcentagem dividendo distribuido nos últimos 12 meses.

        Returns:
            float: DY em porcentagem dos ultimos 12 meses

        Exemplos:
            >>> buscar_indicadores("BBAS3")
            8.958265726043503
        """
        # Pega os dividendos históricos
        proventos = ticker.dividends

        # Filtra apenas os últimos 12 meses
        uma_ano_atras = datetime.now() - timedelta(days=365)
        # Garante que o índice (data) não tenha fuso horario
        proventos.index = proventos.index.tz_localize(None)  # type:ignore

        ultimos_12_meses = proventos[proventos.index >= uma_ano_atras]
        total_dividendos = ultimos_12_meses.sum()

        # Pega o preço atual do ativo
        preco_atual = ticker.info.get("currentPrice")

        if preco_atual and total_dividendos > 0:
            dy_real = (total_dividendos / preco_atual) * 100
            return dy_real
        else:
            return 0.0

    # Adiciona .SA se não tiver
    ticker = (
        yf.Ticker(f"{ticker_name}.SA")
        if not ticker_name.lower().endswith(".sa")
        else yf.Ticker(ticker_name)
    )
    info = ticker.info

    # Extração dos dados
    dados = {
        "Ticker": ticker_name,
        "CotacaoAtual": info.get("currentPrice"),
        "LPA (Lucro por Acao)": info.get("trailingEps"),
        "VPA (Valor Patrimonial por Acao)": info.get("bookValue"),
        "P/VP": info.get("priceToBook"),
        "ROE": info.get("returnOnEquity"),
        "DY (Dividend Yield)": calcular_dy_real() / 100,
    }
    return dados


def listar_ativos_brasileiros(token_brapi: str) -> list:
    """
    Listar todas as ações brasileiras.

    Args:
        token_brapi (str): Token API da Brapi que você pode conseguir no site https://brapi.dev/.

    Returns:
        list: Retorna todos tickers de ativo de ações brasileiras.

    Exemplos:
        >>> listar_ativos_brasileiros("seu_token")
        ["BBAS3","VALE3","GOAU3","GOAU4","SAPR3","CMIG3","CMIG4",...]
    """
    url = f"https://brapi.dev/api/quote/list?token={token_brapi}"

    response = requests.get(url)
    data = response.json()

    contagem = 0
    empresas = []
    # Exibir os tickers das ações
    for stock in data["stocks"]:
        if validar_codigo(stock["stock"]):
            empresas.append(stock["stock"])
            contagem += 1

    return empresas

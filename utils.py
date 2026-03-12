import re

import requests
from bs4 import BeautifulSoup


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
        'DY (Dividend Yield)': 0.0579
        }
    """
    # Vou fazer Web Scraping para pegar as informações das ações
    url = f"https://investidor10.com.br/acoes/{ticker_name}"

    header = {
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=header)

    bs = BeautifulSoup(response.text, "html.parser")

    info = {
        "cotacao": None,
        "lpa": None,
        "vpa": None,
        "p/vp": None,
        "roe": None,
        "dividend yield": None,
    }
    indicadores = bs.find_all("div", class_="cell")

    for indicador in indicadores:
        try:
            nome_indicador = (
                indicador.find(
                    "span", class_="d-flex justify-content-between align-items-center"
                )
                .text.strip()
                .lower()
            )
        except AttributeError:
            continue
        for key in info.keys():
            if key in nome_indicador:
                info[key] = float(
                    indicador.find("div", class_="value")
                    .text.strip()
                    .replace(",", ".")
                    .replace("%", "")
                )

    cotacao = (
        (bs.find("span", class_="value").text)
        .replace("R$", "")
        .replace(",", ".")
        .strip()
    )

    info["cotacao"] = float(cotacao)

    # Extração dos dados
    dados = {
        "Ticker": ticker_name,
        "CotacaoAtual": info.get("cotacao"),
        "LPA (Lucro por Acao)": info.get("lpa"),
        "VPA (Valor Patrimonial por Acao)": info.get("vpa"),
        "P/VP": info.get("p/vp"),
        "ROE": info.get("roe") / 100,
        "DY (Dividend Yield)": info.get("dividend yield") / 100,
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

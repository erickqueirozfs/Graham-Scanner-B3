"""
Objetivo:
Saber quais ações da bolsa estão baratas ou não segundo metodo de graham.

Decidi fazer com a API Brapi que tem que pegar o tokem gratuito que está funcionando até o momento. Para você pegar o token Brapi basta acessar o site https://brapi.dev/ fazer login e obter a chave API.

quais informações vou precisar?
Obrigatorios para calculo de Graham:
- Cotação Atual
- LPA
- VPA
Opcionais, mas vou colocar só para deixar melhor a ánalise:
- PVP
- ROE
- DY
"""

# opções para o script em python
# 1-Via API Brapi e logo depois fazer requisição com o Yfinance
# 2- Instalar as ações do indice ibovespa e usar Yfinance para pegar as cotações e etc
# 3- WEB Scraping em algum site de investimento que nem Investidor10
import math
import os
import time

import pandas as pd
from dotenv import load_dotenv

import utils

# carregando variaveis de ambiente
load_dotenv()


token = os.getenv("TOKEN_BRAPI")
if not token:
    raise Exception("Sem token inserido")

acoes = utils.listar_ativos_brasileiros(token)

dados_acoes = []
for acao in acoes:
    # dando um tempinho para não travar ou recebermos um bloqueio do site
    time.sleep(5)
    # buscando indicadores da ação
    indicadores = utils.buscar_indicadores(acao)

    try:
        lpa = (
            0
            if float(indicadores["LPA (Lucro por Acao)"]) < 0
            else float(indicadores["LPA (Lucro por Acao)"])
        )
    except TypeError:
        lpa = 0
    try:
        vpa = (
            0
            if float(indicadores["VPA (Valor Patrimonial por Acao)"]) < 0
            else float(indicadores["VPA (Valor Patrimonial por Acao)"])
        )
    except TypeError:
        vpa = 0

    # calculo de Graham
    valor_intriseco = math.sqrt(22.5 * lpa * vpa)

    indicadores["ValorIntriseco"] = valor_intriseco
    # Calculo da margem de segurança
    indicadores["MargemSeguranca"] = (
        valor_intriseco - indicadores["CotacaoAtual"]
    ) / indicadores["CotacaoAtual"]

    dados_acoes.append(indicadores)

df = pd.DataFrame(dados_acoes)

acoes_baratas = df.loc[df["MargemSeguranca"] > 0]

writer = pd.ExcelWriter("AcoesBaratasSegundoMTDGraham.xlsx", engine="xlsxwriter")
acoes_baratas.to_excel(writer, index=False)

# colocando a porcentagem nas colunas DY e ROE
workbook = writer.book
worksheet = writer.book.worksheets()[0]  # type:ignore

formato_porcentagem = workbook.add_format({"num_format": "0.00%"})  # type:ignore

# Aplicando o formato nas colunas específicas
# set_column(coluna_inicio, coluna_fim, largura, formato)
worksheet.set_column("F:G", 12, formato_porcentagem)  # type:ignore
worksheet.set_column("I:I", 12, formato_porcentagem)  # type:ignore

writer.close()

# Graham Scanner B3

Esse projeto foi feito com a necessidade de saber quais ações do mercado brasileiro estão baratas segundo o **Método de Graham** e apresentam oportunidade de compra baseada em fundamentos. Com o resultado gerado em Excel, você pode filtrar as melhores oportunidades e aprofundar sua análise para ver quais se encaixam no seu perfil de investidor.

> [!WARNING]
> **Atenção:** Este projeto é uma ferramenta de estudo e automação. O resultado gerado **não é uma recomendação de compra ou venda** de ativos! O mercado financeiro envolve riscos.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Para rodar este script, você precisará de:

* **Python 3.8** ou superior.
* Uma chave de API (Token) da **Brapi** (obtenha gratuitamente em [brapi.dev](https://brapi.dev/)).
* Uma IDE de sua preferência (VS Code, PyCharm, etc.).

### 🔧 Instalação

Siga o passo a passo para configurar o ambiente:

1. **Clone o repositório:**
```bash
git clone https://github.com/erickqueirozfs/Graham-Scanner-B3.git
cd Graham-Scanner-B3

```


2. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate     # No Windows

```


3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```


4. **Configure suas variáveis de ambiente:**
Crie um arquivo `.env` na raiz do projeto e adicione seu token da Brapi:
```env
TOKEN_BRAPI=seu_token_aqui

```


5. **Execute o script:**
```bash
python main.py

```



Ao finalizar, um arquivo chamado `AcoesBaratasSegundoMTDGraham.xlsx` será gerado na pasta do projeto.

## 📦 Implantação

Para utilizar em um sistema ativo (como um bot diário):

1. Hospede o script em um serviço como **GitHub Actions** ou um servidor **VPS**.
2. Agende a execução (Cron Job) para rodar após o fechamento do pregão da B3.
3. Certifique-se de que a variável de ambiente `TOKEN_BRAPI` esteja configurada no ambiente de produção.

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem base.
* [yfinance](https://aroussi.com/post/python-yahoo-finance) - Coleta de dados históricos e fundamentalistas.
* [Brapi](https://brapi.dev/) - Listagem de ativos atualizados da B3.
* [Pandas](https://pandas.pydata.org/) - Manipulação e análise de dados.
* [XlsxWriter](https://xlsxwriter.readthedocs.io/) - Formatação e geração do relatório Excel.

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://www.google.com/search?q=https://github.com/seu-usuario/projeto/blob/main/COLABORACAO.md) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de *pull request*.

## ✒️ Autores

* **Erick Queiroz** - *Desenvolvimento e Idealização* - ([https://github.com/erickqueirozfs](https://github.com/erickqueirozfs))

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 🎁 Expressões de gratidão

* Compartilhe este projeto com outros investidores que buscam automação 📢;
* Contribua com melhorias no código (filtros de dívida, ROE, etc.) 🫂;
* Fique à vontade para abrir uma *Issue* se encontrar algum erro 🐛;

---

⌨️ com ❤️ por Erick Queiroz 😊

---

```markdown
# Contribuindo com o Graham Scanner B3 🚀

Primeiramente, muito obrigado por dedicar seu tempo para contribuir com este projeto! É a ajuda da comunidade que torna as ferramentas de análise de dados financeiros mais acessíveis e precisas.

Ao contribuir, você ajuda outros investidores e estudantes de programação a automatizarem suas análises.

## 📌 Como posso contribuir?

### 1. Relatando Bugs
Se você encontrar um erro no cálculo, uma falha na conexão com a API ou um problema na geração do Excel:
* Verifique se o erro já foi relatado na aba **Issues**.
* Caso não, abra uma nova issue detalhando:
    * O que aconteceu.
    * O passo a passo para reproduzir o erro.
    * O print do erro (se houver).

### 2. Sugerindo Melhorias
Ideias para tornar o scanner mais robusto são muito bem-vindas! Exemplos:
* Adicionar filtros de segurança (ex: Dívida Líquida/EBITDA < 3).
* Incluir novos indicadores como o Preço Justo de Bazin.
* Melhorar a performance das requisições ao Yahoo Finance.

### 3. Enviando Alterações (Pull Requests)
Se você quer colocar a mão na massa:
1. Faça um **Fork** do projeto.
2. Crie uma branch para sua modificação:
   ```bash
   git checkout -b feature/minha-melhoria

```

3. Mantenha o estilo de codificação (PEP 8).
4. Certifique-se de que o cálculo matemático do Valor Intrínseco está correto.
5. Faça o commit de suas alterações:
```bash
git commit -m 'Adiciona filtro de endividamento'

```


6. Envie para o seu fork e abra um **Pull Request**.

## ⚖️ Padrões de Código

* **Documentação:** Mantenha as Docstrings das funções atualizadas.
* **Segurança:** Nunca envie seu arquivo `.env` com sua chave da Brapi para o repositório.
* **Simplicidade:** O foco do projeto é ser didático e eficiente.

## 🤝 Código de Conduta

Seja respeitoso e cordial nas discussões. Estamos todos aqui para aprender e construir algo útil!

---

Qualquer dúvida, sinta-se à vontade para abrir uma discussão nas Issues.
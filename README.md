# PDF Extractor para CCB (Cédula de Crédito Bancário)

Este projeto tem como objetivo extrair dados específicos de um arquivo PDF de Cédula de Crédito Bancário (CCB) e salvar esses dados em formato JSON.

## Estrutura do Projeto

O projeto é composto por dois arquivos principais:

*   `pdf_extractor.py`: Contém a classe `PDFExtractor` responsável por extrair os dados do PDF.
*   `main.py`: Script principal que utiliza a classe `PDFExtractor` para extrair os dados e salvar em um arquivo JSON.

## Arquitetura

A arquitetura do projeto é simples e direta:

1.  **Leitura do PDF:** O script `main.py` instancia a classe `PDFExtractor`, passando o nome do arquivo PDF como parâmetro.
2.  **Extração dos Dados:** A classe `PDFExtractor` utiliza a biblioteca `PyPDF2` para ler o conteúdo do PDF. Em seguida, utiliza expressões regulares (`re` module) para encontrar e extrair os dados relevantes.
3.  **Validação (Implícita):** As expressões regulares atuam como uma forma de validação, garantindo que os dados extraídos correspondam aos padrões esperados.
4.  **Carga:** Os dados extraídos são armazenados em um dicionário Python e, em seguida, salvos em um arquivo JSON usando o módulo `json`.

## Passo a Passo

1.  **Instalação das Dependências:**

    Certifique-se de ter o Python instalado (versão 3.6 ou superior). Em seguida, instale as dependências necessárias usando o pip:

    ```bash
    pip install PyPDF2
    ```

2.  **Execução:**

    Coloque o arquivo PDF (`CCB---DANIEL-BORGES-RODRIGUES.pdf`) no mesmo diretório dos scripts e execute o `main.py`:

    ```bash
    python main.py
    ```

    Isso irá gerar um arquivo `dados_ccb.json` com os dados extraídos.

## Detalhes Técnicos

### Parsing do Arquivo

A função `extract_data` na classe `PDFExtractor` é responsável por ler o arquivo PDF e extrair os dados.

1.  **Leitura do Conteúdo:** Utiliza a biblioteca `PyPDF2` para abrir o arquivo PDF e extrair o texto da primeira página.

    ```python
### with open(self.pdf_file, 'rb') as file:

| reader = PyPDF2.PdfReader(file) |
|---|


        page = reader.pages[0]
        self.text = page.extract_text()
    ```

2.  **Limpeza do Texto:** Realiza substituições para lidar com caracteres especiais, como espaços não separáveis (`\xa0`) e a ligadura "ﬁ", que podem atrapalhar a extração dos dados.

    ```python
    self.text = self.text.replace('\xa0', ' ').replace('ﬁ', 'fi')
    ```

3.  **Extração com Expressões Regulares:** Utiliza expressões regulares para encontrar padrões específicos no texto e extrair os dados desejados. Cada dado é extraído usando a função `_extract_value` ou `_extract_text`, que aplicam as expressões regulares e retornam os valores encontrados.

    Exemplo:

    ```python
    data['data_emprestimo'] = self._extract_date(self.text, r'4\.1 - Data do empréstimo/ ?financiamento:\s*(\d{2}/\d{2}/\d{4})\.')
    ```

### Validação

As validações implementadas são feitas principalmente através das expressões regulares. Cada expressão regular é projetada para corresponder a um padrão específico no texto do PDF. Se a expressão regular não encontrar uma correspondência, a função `_extract_value` ou `_extract_text` retornará `None`, indicando que a validação falhou para aquele campo.

Além disso, há uma validação implícita na conversão dos valores extraídos para o tipo de dado correto. Por exemplo, a função `_extract_value` tenta converter os valores extraídos para `float`. Se a conversão falhar, um erro é impresso e o valor é retornado como `None`.

```python
### def _extract_value(self, text, pattern):

| match = re.search(pattern, text) |
|---|


### if match:

| value = match.group(1).replace('.', '').replace(',', '.') |
|---|


### try:

| return float(value) |
|---|


### except ValueError:

| print(f"Erro ao converter para float: {value}") |
|---|


                return None
### else:

| print(f"Padrão não encontrado: {pattern}") |
|---|

            return None

Carga
A carga dos dados é feita em duas etapas:

Armazenamento em Dicionário: Os dados extraídos são armazenados em um dicionário Python, onde as chaves são os nomes dos campos (por exemplo, data_emprestimo, valor_credito) e os valores são os dados extraídos.
data = {}
data['data_emprestimo'] = self._extract_date(self.text, r'4\.1 - Data do empréstimo/ ?financiamento:\s*(\d{2}/\d{2}/\d{4})\.')
# ... outros campos
Salvamento em JSON: O dicionário com os dados é então salvo em um arquivo JSON usando o módulo json. A função json.dump é utilizada para converter o dicionário em formato JSON e salvar no arquivo.
with open(json_file, 'w', encoding='utf-8') as file:
json.dump(data, file, indent=4, ensure_ascii=False)
```
*   `indent=4` formata o JSON com 4 espaços de indentação para melhor legibilidade.
*   `ensure_ascii=False` garante que caracteres não ASCII sejam salvos corretamente.

Considerações Finais
Este projeto fornece uma base sólida para extrair dados de arquivos PDF de CCB. As expressões regulares podem ser ajustadas para lidar com variações no formato do PDF. Além disso, validações mais robustas podem ser implementadas para garantir a qualidade dos dados extraídos.

**Como usar:**

1.  Copie o conteúdo acima e salve em um arquivo chamado `README.md` no diretório raiz do seu projeto.
2.  Certifique-se de que os arquivos `pdf_extractor.py`, `main.py` e o arquivo PDF de exemplo (`CCB---DANIEL-BORGES-RODRIGUES.pdf`) estejam no mesmo diretório.
3.  Faça o upload de todos os arquivos para o seu repositório no GitHub.

Este `README.md` fornece uma visão geral completa do seu projeto, incluindo a estrutura, arquitetura, detalhes técnicos e um passo a passo para executar o código.


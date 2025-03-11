import json
from pdf_extractor import PDFExtractor  # Certifique-se de que o nome do arquivo está correto

# Nome do arquivo PDF
pdf_file = 'CCB - DANIEL BORGES RODRIGUES.pdf'

# Criar uma instância da classe PDFExtractor
pdf_extractor = PDFExtractor(pdf_file)

# Extrair os dados
data = pdf_extractor.extract_data()

# Nome do arquivo JSON
json_file = 'dados_ccb.json'

# Abrir o arquivo JSON em modo de escrita
with open(json_file, 'w', encoding='utf-8') as file:
    # Salvar os dados em formato JSON
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f'Dados salvos em {json_file}')
import PyPDF2
import re
import unicodedata

class PDFExtractor:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.text = None

    def extract_data(self):
        data = {}
        with open(self.pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page = reader.pages[0]
            self.text = page.extract_text()

        # Substituir espaços não separáveis e "ﬁ"
        self.text = self.text.replace('\xa0', ' ').replace('ﬁ', 'fi')

        data['data_emprestimo'] = self._extract_date(self.text, r'4\.1 - Data do empréstimo/ ?financiamento:\s*(\d{2}/\d{2}/\d{4})\.')
        data['valor_credito'] = self._extract_value(self.text, r'Valor do crédito:\s*R\$ ([\d,\.]+)')
        data['taxa_juros_am'] = self._extract_value(self.text, r'4\.9.*:\s*([\d,\.]+)')
        data['taxa_juros_am_cet'] = self._extract_value(self.text, r'4\.11.*:\s*([\d,\.]+)')
        data['taxa_juros_aa'] = self._extract_value(self.text, r'4\.10.*R\$\s*([\d,\.]+)')
        data['nome'] = self._extract_text(self.text, r'Nome:\s*([\w\s]+)CPF:')
        data['cpf'] = self._extract_text(self.text, r'Nome: DANIEL BORGES RODRIGUES CPF: ([\d\.-]+)')

        if data['taxa_juros_am'] is None and data['taxa_juros_am_cet'] is not None:
            data['taxa_juros_am'] = data['taxa_juros_am_cet']

        return data

    def _extract_date(self, text, pattern):
        match = re.search(pattern, text)
        return match.group(1) if match else None

    def _extract_value(self, text, pattern):
        match = re.search(pattern, text)
        if match:
            value = match.group(1).replace('.', '').replace(',', '.')
            try:
                return float(value)
            except ValueError:
                print(f"Erro ao converter para float: {value}")
                return None
        else:
            print(f"Padrão não encontrado: {pattern}")
            return None

    def _extract_text(self, text, pattern):
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None
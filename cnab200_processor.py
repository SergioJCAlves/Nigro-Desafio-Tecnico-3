import csv
from registro_cnab200 import RegistroCNAB200

class CNAB200Processor:
    def __init__(self, data):
        self.data = data
        self.registro = self._criar_registro()

    def _criar_registro(self):
        return RegistroCNAB200(
            data_emprestimo=self.data.get('data_emprestimo'),
            valor_credito=self.data.get('valor_credito'),
            taxa_juros_am=self.data.get('taxa_juros_am'),
            taxa_juros_aa=self.data.get('taxa_juros_aa'),
            nome=self.data.get('nome'),
            cpf=self.data.get('cpf')
        )

    def validate(self):
        self.registro.validar()

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['data_emprestimo', 'valor_credito', 'taxa_juros_am', 'taxa_juros_aa', 'nome', 'cpf']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(self.registro.__dict__)

    def get_registro(self):
        return self.registro
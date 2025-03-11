from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Header:
    banco: str
    agencia: str
    data_hora_geracao: datetime
    nome_empresa: str
    nome_arquivo: str

@dataclass
class Detalhe:
    banco: str
    nosso_numero: str
    numero_documento: str
    data_vencimento: datetime
    valor_titulo: float
    data_pagamento: datetime
    valor_pago: float
    cpf_cnpj_pagador: str
    nome_pagador: str

@dataclass
class Trailer:
    quantidade_registros: int
    soma_valores_pagos: float

class CNAB200Parser:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.header = None
        self.detalhes = []
        self.trailer = None

    def parse(self):
        with open(self.arquivo, 'r') as f:
            linhas = f.readlines()
        
        self._parse_header(linhas[0])
        for linha in linhas[1:-1]:
            self._parse_detalhe(linha)
        self._parse_trailer(linhas[-1])

    def _parse_header(self, linha: str):
        self.header = Header(
            banco=linha[0:3],
            agencia=linha[3:7],
            data_hora_geracao=datetime.strptime(linha[7:17], '%Y%m%d%H'),
            nome_empresa=linha[17:37].strip(),
            nome_arquivo=linha[37:57].strip()
        )

    def _parse_detalhe(self, linha: str):
        detalhe = Detalhe(
            banco=linha[1:4],
            nosso_numero=linha[4:14],
            numero_documento=linha[14:24],
            data_vencimento=datetime.strptime(linha[24:32], '%Y%m%d'),
            valor_titulo=float(linha[32:42]) / 100,
            data_pagamento=datetime.strptime(linha[42:50], '%Y%m%d'),
            valor_pago=float(linha[50:62]) / 100,
            cpf_cnpj_pagador=linha[62:77],
            nome_pagador=linha[77:107].strip()
        )
        self.detalhes.append(detalhe)

    def _parse_trailer(self, linha: str):
        self.trailer = Trailer(
            quantidade_registros=int(linha[1:7]),
            soma_valores_pagos=float(linha[7:20]) / 100
        )
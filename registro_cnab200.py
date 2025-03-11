class RegistroCNAB200:
    def __init__(self, data_emprestimo, valor_credito, taxa_juros_am, taxa_juros_aa, nome, cpf):
        self.data_emprestimo = data_emprestimo
        self.valor_credito = valor_credito
        self.taxa_juros_am = taxa_juros_am
        self.taxa_juros_aa = taxa_juros_aa
        self.nome = nome
        self.cpf = cpf

    def validar(self):
        assert self.data_emprestimo is not None, "Data do empréstimo não encontrada"
        assert self.valor_credito is not None, "Valor do crédito não encontrado"
        assert self.taxa_juros_am is not None, "Taxa de juros a.m. não encontrada"
        assert self.taxa_juros_aa is not None, "Taxa de juros a.a. não encontrada"
        assert self.nome is not None, "Nome não encontrado"
        assert self.cpf is not None, "CPF não encontrado"

    def __str__(self):
        return f"Data: {self.data_emprestimo}, Valor: {self.valor_credito}, Juros AM: {self.taxa_juros_am}, Juros AA: {self.taxa_juros_aa}, Nome: {self.nome}, CPF: {self.cpf}"
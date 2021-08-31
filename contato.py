
class Contato:
    def __init__(self, nome: str, telefone: int) -> None:
        self.nome = nome
        self.telefone = telefone

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nTelefone: {self.telefone}'

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def telefone(self) -> int:
        return self._telefone

    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
    
    @telefone.setter
    def telefone(self, telefone: int) -> None:
        self._telefone = telefone


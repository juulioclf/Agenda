from contato import Contato
from repositorio import RepositorioContatos

class CadastroContatos:
    def __init__(self) -> None:
        self.repositorio = RepositorioContatos()


    def __str__(self):
        for contato in self.repositorio:
            return contato


    def incluir(self, contato: Contato) -> bool:

        resultado = None
        if self.repositorio.existe(contato):
            input('esse contato ja existe, tecle enter para continuar...')
        else:
            resultado = self.repositorio.incluir(contato)
            return resultado


    def alterar(self, nome_old: str, telefone_new: str) -> None:

        resultado = None
        if not self.repositorio.alterar(nome_old, telefone_new):
            input('esse contato nao existe, tecle enter para continuar...')

        else:
            resultado = self.repositorio.alterar(nome_old, telefone_new)


        return resultado


    def excluir(self, contato: Contato) -> Contato:

        resultado = None
        if self.repositorio.consultar_id(contato) == None:
            input('digite um id valido, tecle enter para continuar...')
        
        else:
            resultado = self.repositorio.excluir(contato)

        return resultado

    
    def consultar(self, contato: Contato) -> Contato:

        resultado = None
        if self.repositorio.existe(contato):
            resultado = contato

        return resultado

    


from contato import Contato

class RepositorioContatos:

    def __init__(self) -> None:

        self.armazenador = []
        self.lixeira = []


    def existe(self, cls) -> bool:

        data_cls = {'nome': cls.nome, 'telefone': cls.telefone}
        
        if data_cls in self.armazenador:
            return True
        return False

    
    def incluir(self, cls) -> bool:
        
        resultado = False
        if not self.existe(cls):
            self.armazenador.append({'nome': cls.nome, 'telefone': cls.telefone})
            resultado = True

        return resultado
        


    def alterar(self, nome_old: str, telefone_new: str) -> bool:
        resultado = False

        for contato in self.armazenador:
            if contato['nome'] == nome_old:
                index = self.consultar_id(contato)
                self.armazenador[index]['telefone'] = telefone_new
                resultado = True

        return resultado


    def consultar_id(self, nome) -> bool:
        
        for contato in self.armazenador:
            if contato['nome'] == nome:
                return self.armazenador.index(contato)
            
        return False
            

    def excluir(self, id) -> bool:
        if id < 0 or id > len(self.armazenador) -1 :
            resultado = False
        else:
            self.lixeira.append(self.armazenador[id])
            self.armazenador.pop(id)
            resultado = True
        
        return resultado
        


if __name__ == "__main__":

    #init
    p1 = Contato('julio', 929921035522)
    p2 = Contato('gabe', 11112321313)
    p3 = Contato('neto', 11112321313)
    p4 = Contato('francisco', 11112321313)
    i = RepositorioContatos()

    #testes include
    print(i.incluir(p1))
    print(i.incluir(p1))
    print(i.incluir(p2))
    print(i.incluir(p3))
    print(i.incluir(p4))
    print(i.armazenador)

    #testes update
    p3 = Contato('julio alterado', 21321321)
    print(i.alterar(p1, p3))
    print(i.armazenador)

    #testes delete
    print(i.excluir(4))
    print(i.excluir(3))

    #testes cosulta por id
    print(i.consultar_id('francisco'))
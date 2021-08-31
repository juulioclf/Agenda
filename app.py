from contato import Contato
from cadastro import CadastroContatos
from os import system
from time import sleep


class ContatoApp:
    def __init__(self) -> None:
        self.regras_negocio = CadastroContatos()  
        self.start = self.opcao_desejada()

    def exibe_menu(self):
        self.limpa_tela()
        print("1. Incluir novo contato")
        print("2. Alterar telefone de um contato")
        print("3. Excluir um contato")
        print("4. Consultar contato por nome")
        print("5. Listar todos os contatos")
        print("6. Sair")


    def limpa_tela(self):
        system("CLS")

    def tempo_espera(self):
        sleep(2)
   

    def ler_entrada(self):
        nome = input("digite o nome: ")
        telefone = input("digite o telefone: ")
        resultado = Contato(nome, telefone)
        return resultado
        

    def ler_opcao(self):
        opcao = int(input("digite a opcao desejada: ")) 
        return opcao


    def opcao_desejada(self):
        
        opcao = -1

        while opcao != 6:

            self.exibe_menu()
            opcao = self.ler_opcao()
        
            if opcao == 1:
                self.limpa_tela()
                contato = self.ler_entrada()
                
                if self.regras_negocio.incluir(contato) != None:
                    print("Nome e Telefone adicionados na lista de contatos!")
                    self.tempo_espera()
        

            elif opcao == 2:
                #da pra melhorar
                self.limpa_tela()
                nome_old = input("digite o nome que voce deseja alterar: ")
                telefone_new = input("digite o novo numero: ")

                if self.regras_negocio.alterar(nome_old, telefone_new) != None:
                    print("Nome e Telefone alterados!")
                    self.tempo_espera()


            elif opcao == 3:
                self.limpa_tela()
                resultado = self.ler_entrada()
                if self.regras_negocio.excluir(resultado) != None:
                    print(f"{resultado.nome} excluido!")
                    self.tempo_espera()


            elif opcao == 4:
                self.limpa_tela()
                resultado = self.ler_entrada()

                if self.regras_negocio.consultar(resultado) != None:
                    print(self.regras_negocio.consultar(resultado))
                    self.tempo_espera()
                

            elif opcao == 5:
                self.limpa_tela()
                for contato in self.regras_negocio.repositorio:
                    print(contato)
                self.tempo_espera()

            elif opcao == 6:
                self.limpa_tela()
                print("saindo do sistema...")
                self.tempo_espera()
                break

            else:
                self.limpa_tela()
                print("digite uma entrada valida")
                self.tempo_espera()
                continue


if __name__ == "__main__":
    app = ContatoApp()
    # print("melhorar o excluir contato")
    # print("melhorar o consultar por nome")
    # print("melhorar o listar todos")
    # input()
    
    

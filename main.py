from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def get_tipo(self):
        pass

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_alugados = []

    def alugar_livro(self, livro):
        if len(self.livros_alugados) < 3 and livro.esta_disponivel():
            self.livros_alugados.append(livro)
            livro.alterar_disponibilidade(False)
            print(f"{livro.titulo} alugado para {self.nome}")
        else:
            print(f"{self.nome} já atingiu o limite ou o livro não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_alugados:
            self.livros_alugados.remove(livro)
            livro.alterar_disponibilidade(True)
            print(f"{livro.titulo} devolvido por {self.nome}.")
        else:
            print(f"{self.nome} não possui o livro {livro.titulo}.")

    def get_tipo(self):
        return "Usuário Comum"

class Administrador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def cadastrar_livro(self, sistema, livro):
        sistema.adicionar_livro(livro)
        print(f"Livro {livro.titulo} cadastrado com sucesso!")

    def get_tipo(self):
        return "Administrador"

class ItemSistema(ABC):
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    @abstractmethod
    def esta_disponivel(self):
        pass

    def alterar_disponibilidade(self, status):
        self.disponivel = status

class Livro(ItemSistema):
    def esta_disponivel(self):
        return self.disponivel

class Sistema:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def livros_disponiveis(self):
        return [livro for livro in self.livros if livro.esta_disponivel()]

    def exibir_livros_disponiveis(self):
        disponiveis = self.livros_disponiveis()
        print("Livros disponíveis:")
        for livro in disponiveis:
            print(f"{livro.titulo} - {livro.autor}")

    def exibir_usuarios_com_livros(self, usuarios):
        print("Usuários com livros alugados:")
        for usuario in usuarios:
            if usuario.livros_alugados:
                print(f"{usuario.nome}: {[livro.titulo for livro in usuario.livros_alugados]}")


# Exemplo
if __name__ == "__main__":
    sistema = Sistema()

    admin = Administrador("Carlos", 40)

    livro1 = Livro("Python Básico", "João Silva", 2021)
    livro2 = Livro("Algoritmos", "Maria Clara", 2019)
    livro3 = Livro("Introdução a HTML", "João Azevedo",2010)

    admin.cadastrar_livro(sistema, livro1)
    admin.cadastrar_livro(sistema, livro2)
    admin.cadastrar_livro(sistema, livro3)

    usuario1 = UsuarioComum("Ana", 25, "12345")
    usuario2 = UsuarioComum("Pedro", 30, "67890")

    usuario1.alugar_livro(livro1)
    usuario2.alugar_livro(livro1) 
    usuario1.devolver_livro(livro1)
    usuario2.alugar_livro(livro1) 

    sistema.exibir_livros_disponiveis()
    sistema.exibir_usuarios_com_livros([usuario1, usuario2])

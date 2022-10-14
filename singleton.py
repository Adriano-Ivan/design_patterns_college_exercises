

class SiteConfiguration:

    _instance = None
    _numeroDeVisitantes = 0

    def __init__(self):
        self.titulo = "TESTE"
        self.subtitulo = "TESTE SUBTÍTULO"
        self.email = "EMAIL@EMAIL.COM"

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def exibirInformacoes(self):
        print()
        print("*"*20)
        print(f"Informações: {self.titulo} (título), {self.subtitulo} (subtítulo), {self.email} (email)")
        print(f"Visitantes: {self._numeroDeVisitantes}")
        print("*"*20)

    def adicionarVisitante(self):
        self._numeroDeVisitantes+=1


class Cliente:

    def __init__(self, config):
        config.adicionarVisitante()
        self._imprimirInformacoes(config)

    def _imprimirInformacoes(self,config):
        config.exibirInformacoes()

conf1 = SiteConfiguration()
conf2 = SiteConfiguration()

cli1 = Cliente(conf1)
cli2 = Cliente(conf2)
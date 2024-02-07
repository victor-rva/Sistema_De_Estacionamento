from datetime import datetime
class Veiculo:
    def __init__(self, placa):
        """
        Classe que representa um veículo no estacionamento.
        Argumentos:
        placa (str): Placa do veículo.
        """
        self.placa = placa
        self.hora_entrada = datetime.now()
        self.hora_saida = None
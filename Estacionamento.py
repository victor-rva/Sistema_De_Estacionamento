from datetime import datetime
class Estacionamento:
    def __init__(self):
        """
        Classe que representa o estacionamento.
        Inicializa o estacionamento com um dicionário de vagas vazio.
        """
        self.vagas = {i: [] for i in range(1, 41)}
    
    def estacionar(self, veiculo):
        """
        Estaciona um veículo no estacionamento.

        Argumentos:
        veiculo (Veículo): Veículo a ser estacionado.

        Returns:
        int or None: Número da vaga onde o veículo foi estacionado ou None se não houver vagas disponíveis.
        """
        for vaga, carros in self.vagas.items():
            if not carros:
                carros.append(veiculo)
                return vaga
        return None

    def saida(self, placa):
        """
        Registra a saída de um veículo do estacionamento.

        Argumentos:
        placa (str): Placa do veículo a ser retirado.

        Returns:
        int or None: Número da vaga da qual o veículo foi retirado ou None se o veículo não for encontrado.
        """
        for vaga, carros in self.vagas.items():
            for carro in carros:
                if carro.placa == placa:
                    carro.hora_saida = datetime.now()
                    carros.remove(carro)
                    return vaga
        return None

    def resumo_ocupacao(self):
        """
        Exibe um resumo da ocupação do estacionamento.
        """
        for vaga, carros in self.vagas.items():
            print(f"Vaga {vaga}:")
            if not carros:
                print("Vaga livre")
            else:
                for carro in carros:
                    print(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}", end="")
                    if carro.hora_saida is not None:
                        print(f" - Saída: {carro.hora_saida.strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        print(" - Ainda estacionado")
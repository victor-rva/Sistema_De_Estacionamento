import json
# importa o módulo json, que será utilizado para carregar e salvar dados no formato JSON
import os
# importa o módulo os, que fornece funções relacionadas ao sistema operacional, como verificar a existência de arquivos.
from datetime import datetime

from Veiculo import Veiculo
from Estacionamento import Estacionamento

estacionamento = Estacionamento()

if os.path.exists("estacionamento.txt") or os.path.exists("estacionamento.json"):
    #O programa verifica se os arquivos "estacionamento.txt" ou "estacionamento.json" existem na pasta atual.
    resposta = input("Deseja carregar os dados de um arquivo TXT ou JSON? (S/N) ")
    if resposta.upper() == "S":
        tipo_arquivo = input("Digite o tipo de arquivo que deseja carregar (TXT ou JSON): ")
        if tipo_arquivo.upper() == "TXT" and os.path.exists("estacionamento.txt"):
            # Código para popular o dicionário a partir do arquivo TXT. Se um dos arquivos existir,
            # solicite ao usuário que escolha se deseja carregar os dados de um arquivo.
            with open("estacionamento.txt", "r") as arquivo_txt:
                for linha in arquivo_txt:
                    vaga_str, info = linha.strip().split(":")
                    vaga = int(vaga_str.split()[1])
                    if info == "Vaga livre":
                        estacionamento.vagas[vaga] = []
                    else:
                        veiculos_info = info.split("\n")
                        for veiculo_info in veiculos_info:
                            if veiculo_info:
                                placa, entrada, saida = veiculo_info.split(" - ")
                                placa = placa.split(": ")[1]
                                entrada = datetime.strptime(entrada.split(": ")[1], "%d/%m/%Y %H:%M:%S")
                                if saida != "Ainda estacionado":
                                    saida = datetime.strptime(saida.split(": ")[1], "%d/%m/%Y %H:%M:%S")
                                else:
                                    saida = None
                                veiculo = Veiculo(placa)
                                veiculo.hora_entrada = entrada
                                veiculo.hora_saida = saida
                                estacionamento.vagas[vaga].append(veiculo)
        elif tipo_arquivo.upper() == "JSON" and os.path.exists("estacionamento.json"):
            # Código para popular o dicionário a partir do arquivo JSON
            with open("estacionamento.json", "r") as arquivo_json:
                dados = json.load(arquivo_json)
                for vaga, carros in dados.items():
                    estacionamento.vagas[int(vaga)] = []
                    for carro in carros:
                        veiculo = Veiculo(carro['placa'])
                        veiculo.hora_entrada = datetime.strptime(carro['hora_entrada'], '%Y-%m-%d %H:%M:%S')
                        if carro['hora_saida']:
                            veiculo.hora_saida = datetime.strptime(carro['hora_saida'], '%Y-%m-%d %H:%M:%S')
                        estacionamento.vagas[int(vaga)].append(veiculo)
        else:
            print("Arquivo não encontrado ou tipo de arquivo inválido")

        while True:
            print("=== Estacionamento X ===")
            print("1- Estacionar")
            print("2- Saída")
            print("3- Resumo de ocupação")
            print("9- Fim")
            escolha = input("Escolha: ")

            if escolha == "1":
                placa = input("Digite a placa do veículo: ")
                veiculo = Veiculo(placa)
                vaga = estacionamento.estacionar(veiculo)
                if vaga:
                    print(f"O veículo foi estacionado na vaga {vaga}")
                else:
                    print("Não há vagas disponíveis")

            elif escolha == "2":
                placa = input("Digite a placa do veículo que deseja retirar: ")
                vaga = estacionamento.saida(placa)
                if vaga:
                    print(f"O veículo foi retirado da vaga {vaga}")
                else:
                    print("Veículo não encontrado")

            elif escolha == "3":
                estacionamento.resumo_ocupacao()

            elif escolha == "9":
                resposta = input("Deseja salvar os dados em um arquivo TXT ou JSON? (S/N) ")
                # Se responder "S" para salvar os  dados em um arquivo TXT ou JSON, o programa solicita ao usuário que digite o tipo de
                # arquivo desejado. Se o tipo for "TXT", o programa abre o arquivo "estacionamento.txt" em modo de escrita
                # e percorre as vagas do estacionamento, escrevendo as informações de cada veículo estacionado no arquivo.
                # Se o tipo for "JSON", o programa abre o arquivo "estacionamento.json" em modo de escrita e utiliza a
                # função json.dump()para salvar o dicionário de vagas do estacionamento no formato JSON.
                if resposta.upper() == "S":
                    tipo_arquivo = input("Digite o tipo de arquivo que deseja salvar (TXT ou JSON): ")
                    if tipo_arquivo.upper() == "TXT":
                        with open("estacionamento.txt", "w") as arquivo_txt:
                            for vaga, carros in estacionamento.vagas.items():
                                arquivo_txt.write(f"Vaga {vaga}:\n")
                                if not carros:
                                    arquivo_txt.write("Vaga livre\n")
                                else:
                                    for carro in carros:
                                        arquivo_txt.write(f"Placa: {carro.placa} - Entrada: {carro.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}\n")
                                        if carro.hora_saida is not None:
                                            arquivo_txt.write(
                                                f" - Saída: {carro.hora_saida.strftime('%d/%m/%Y %H:%M:%S')}\n")
                                        else:
                                            arquivo_txt.write(" - Ainda estacionado\n")
                    elif tipo_arquivo.upper() == "JSON":
                        with open("estacionamento.json", "w") as arquivo_json:
                            json.dump(estacionamento.vagas, arquivo_json, default=str)
                    else:
                        print("Tipo de arquivo inválido")
                break

            else:
                print("Opção inválida")
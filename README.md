# Estacionamento

Este é um programa simples em Python que simula um sistema de estacionamento. O programa utiliza classes para representar veículos e o estacionamento, permitindo estacionar veículos, registrar suas saídas e exibir um resumo da ocupação do estacionamento. Além disso, oferece a opção de carregar e salvar dados em arquivos de texto (TXT) ou formato JSON.

## Funcionalidades

1. **Classe Veiculo:**
   - Representa um veículo no estacionamento.
   - Atributos:
     - `placa`: Placa do veículo.
     - `hora_entrada`: Momento da entrada do veículo no estacionamento.
     - `hora_saida`: Momento da saída do veículo do estacionamento (pode ser `None` se ainda estiver estacionado).

2. **Classe Estacionamento:**
   - Representa o estacionamento.
   - Atributos:
     - `vagas`: Dicionário que mapeia números de vagas para listas de veículos estacionados.

   - Métodos:
     - `estacionar(veiculo)`: Estaciona um veículo no estacionamento, retornando o número da vaga ou `None` se não houver vagas disponíveis.
     - `saida(placa)`: Registra a saída de um veículo do estacionamento, retornando o número da vaga ou `None` se o veículo não for encontrado.
     - `resumo_ocupacao()`: Exibe um resumo da ocupação do estacionamento.

3. **Carregamento de Dados a partir de Arquivos:**
   - Verifica se os arquivos "estacionamento.txt" ou "estacionamento.json" existem.
   - Permite ao usuário escolher carregar os dados de um arquivo TXT ou JSON, se existirem.

4. **Menu Principal:**
   - Permite ao usuário interagir com o programa através de um menu.
   - Opções:
     - Estacionar veículo.
     - Registrar saída de veículo.
     - Exibir resumo da ocupação.
     - Finalizar o programa.

5. **Salvamento de Dados em Arquivos:**
   - Pergunta ao usuário se deseja salvar os dados.
   - Se sim, solicita o tipo de arquivo desejado (TXT ou JSON).
   - Salva os dados no arquivo escolhido.

## Uso do Programa

1. Execute o programa em um ambiente Python.
2. Se os arquivos "estacionamento.txt" ou "estacionamento.json" existirem, o programa pergunta se deseja carregar os dados.
3. Interaja com o programa através do menu, escolhendo as opções disponíveis.
4. Ao finalizar, o programa pergunta se deseja salvar os dados.

## Requisitos

- Python 3.x

## Notas

- Certifique-se de fornecer entradas válidas durante a interação com o programa.
- Os arquivos de dados ("estacionamento.txt" ou "estacionamento.json") são criados ou sobrescritos ao salvar os dados.

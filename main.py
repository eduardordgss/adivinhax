import pandas as pd

while True:
    dados = pd.read_csv('brasileirao.csv')
    times = None

    while not times:
        perguntas = list(dados.columns[1:].values)
        respostas = []
        for pergunta in perguntas:
            respostas.append(dados[pergunta].sum())

        if respostas:
            pergunta_atual = perguntas[respostas.index(max(respostas))]
            resposta_atual = input(f'{pergunta_atual} (S: Sim / N: Não): ')

            if resposta_atual == 'S':
                dados = dados[dados[pergunta_atual] == 1].drop(columns=[pergunta_atual])
            elif resposta_atual == 'N':
                dados = dados[dados[pergunta_atual] == 0].drop(columns=[pergunta_atual])

            if len(dados.index) == 1:
                times = dados['Times'].values[0]
            elif len(dados.index) == 0:
                print('Ops! As resposta foram inconclusivas.')
                dados = pd.read_csv('brasileirao.csv')

    if times:
        print(f'Você pensou em: {times}\n')

    continuar = input('Deseja jogar novamente? (S: Sim / N: Não): ')
    if continuar == 'N':
        break
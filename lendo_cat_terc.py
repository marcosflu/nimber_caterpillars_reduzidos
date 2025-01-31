import matplotlib.pyplot as plt

# Função para ler o arquivo e extrair os valores de Nimber
def extrair_nimbers(nome_arquivo):
    nimbers = []
    with open(nome_arquivo, "r") as file:
        for linha in file:
            # Extrai o valor de Nimber da linha
            if "Nimber" in linha:
                nimber = int(linha.split("Nimber")[1].strip())
                nimbers.append(nimber)
    return nimbers

# Função para plotar o gráfico dos valores de Nimber
def plotar_nimbers(nimbers):
    plt.figure(figsize=(10, 6))
    plt.plot(nimbers, marker='o', linestyle='-', color='b')
    plt.title("Valores de Nimber para Caterpillars Reduzidos")
    plt.xlabel("Índice do Caterpillar")
    plt.ylabel("Valor de Nimber")
    plt.grid(True)
    plt.show()

# Nome do arquivo
nome_arquivo = "nimber_caterpillar_reduzidos_results.txt"

# Extrair os valores de Nimber
nimbers = extrair_nimbers(nome_arquivo)

# Plotar o gráfico
plotar_nimbers(nimbers)
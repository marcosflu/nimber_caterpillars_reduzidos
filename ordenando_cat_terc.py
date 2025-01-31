def decimal_to_ternary(n):
    """Converte um número decimal para sua representação em base 3 (como string)."""
    if n == 0:
        return "0"
    
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary  # Obtém o resto da divisão por 3
        n //= 3  # Divide por 3 para continuar

    return ternary

#def generate_caterpillars(k, max_n=999, output_file="caterpillars.txt"):
def generate_caterpillars(k, max_n=550, output_file="cat_terc_reduzido.txt"):
    """
    Gera os caterpillars do tipo (n, k) para n variando de 3 até max_n e salva em um arquivo.
    
    Parâmetros:
    k - Valor decimal que será convertido para base 3
    max_n - Número máximo de caterpillars a gerar (padrão: 999)
    output_file - Nome do arquivo onde os caterpillars serão salvos
    """
    # Converte k para base 3 e transforma em uma lista de inteiros
    k_ternary = list(map(int, decimal_to_ternary(k)))  # Exemplo: 10 → [1,0,1]
    length_k = len(k_ternary)

    with open(output_file, "w") as file:  # Abre o arquivo para escrita
        for n in range(3, max_n + 1):  # Começa do n=3
            if n < length_k + 2:
                continue  # Garante que k_ternary sempre cabe entre os zeros
            
            num_zeros_left = n - length_k - 1  # Quantidade de zeros antes do k
            caterpillar = [0] * num_zeros_left  # Adiciona zeros antes
            caterpillar.extend(k_ternary)  # Insere os dígitos de k
            caterpillar.append(0)  # Adiciona o zero final

            output_line = f"(n={n}, k={k}): {tuple(caterpillar)}\n"
            file.write(output_line)  # Escreve no arquivo
        
    print(f"Caterpillars salvos em '{output_file}'!")

# Solicita o valor de k ao usuário
k = int(input("Digite o valor de k: "))

# Gera os caterpillars e salva no arquivo
generate_caterpillars(k)
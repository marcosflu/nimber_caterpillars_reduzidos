import itertools

# Cache para memoização
nimber_cache = {}

def mex(s):
    """Calcula o mínimo excludente (mex) de um conjunto s."""
    m = 0
    while m in s:
        m += 1
    return m

def tuple_to_adjacency(caterpillar):
    """Converte uma tupla representando um Caterpillar em uma lista de adjacência."""
    adj = {}
    spine_vertices = list(range(len(caterpillar)))
    leaf_start = len(caterpillar)

    # Conectar vértices da espinha dorsal
    for i in spine_vertices:
        adj[i] = []
        if i > 0:
            adj[i].append(i - 1)
        if i < len(spine_vertices) - 1:
            adj[i].append(i + 1)

    # Adicionar folhas conectadas aos vértices da espinha dorsal
    current_leaf = leaf_start
    for i, num_leaves in enumerate(caterpillar):
        for _ in range(num_leaves):
            adj[i].append(current_leaf)
            adj[current_leaf] = [i]
            current_leaf += 1

    return adj

def get_connected_components(adj):
    """Encontra os componentes conectados de um grafo dado por uma lista de adjacência."""
    visited = set()
    components = []

    for vertex in adj:
        if vertex not in visited:
            stack = [vertex]
            component = set()
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.add(v)
                    stack.extend(adj[v])
            components.append(component)

    return components

def compute_nimber(adj):
    """Calcula o nimber usando a função de Sprague-Grundy."""
    key = frozenset(frozenset(neighbors) for neighbors in adj.values())
    if key in nimber_cache:
        return nimber_cache[key]

    possible_nimbers = set()

    for vertex in list(adj.keys()):
        # Remover o vértice e seus vizinhos
        neighbors = set(adj[vertex])
        removed = neighbors | {vertex}
        new_adj = {v: [u for u in neighbors_list if u not in removed]
                   for v, neighbors_list in adj.items() if v not in removed}

        # Encontrar os componentes conectados
        components = get_connected_components(new_adj)

        # Calcular o nimber para cada componente
        nimber_total = 0
        for component in components:
            subgraph = {v: new_adj[v] for v in component}
            nimber_total ^= compute_nimber(subgraph)

        possible_nimbers.add(nimber_total)

    # Determinar o mex
    current_nimber = mex(possible_nimbers)
    nimber_cache[key] = current_nimber
    return current_nimber

def tuple_to_nimber(caterpillar):
    """Calcula o nimber de um Caterpillar representado como tupla."""
    adj = tuple_to_adjacency(caterpillar)
    return compute_nimber(adj)

# Nome do arquivo de entrada e saída
#input_file = "non_binary_caterpillars.txt"
input_file = "cat_terc_reduzido.txt"
#input_file = "caterpillars.txt"
output_file = "nimber_caterpillar_reduzidos_results.txt"

# Processar o arquivo
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    outfile.write("Resultados:\n")
    for line in infile:
        line = line.strip()
        try:
            # Remover parênteses e vírgulas extras, e converter em tupla de inteiros
            if line.endswith(","):
                line = line[:-1]  # Remove a vírgula final
            caterpillar = tuple(map(int, line.strip("()").split(",")))
            nimber = tuple_to_nimber(caterpillar)
            outfile.write(f"Caterpillar {caterpillar} -> Nimber {nimber}\n")
        except ValueError:
            outfile.write(f"Linha ignorada (formato inválido): {line}\n")

print(f"Os resultados foram salvos no arquivo '{output_file}'.")
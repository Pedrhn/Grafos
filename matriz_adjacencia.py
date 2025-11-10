def criar_grafo():
    return [], []

def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        for linha in matriz:
            linha.append(0)
        matriz.append([0] * len(vertices))

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1

def remover_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        idx = vertices.index(vertice)
        matriz.pop(idx)
        for linha in matriz:
            linha.pop(idx)
        vertices.remove(vertice)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0

def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    return False

def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    return [vertices[j] for j in range(len(vertices)) if matriz[i][j] == 1]

def grau_vertices(matriz, vertices):
    graus = {}
    n = len(vertices)
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[j][i] for j in range(n))
        graus[v] = {"entrada": entrada, "saida": saida, "total": entrada + saida}
    for v, g in graus.items():
        print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")
    return graus

def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True

def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print("Vértice inexistente.")
    else:
        v = vizinhos(matriz, vertices, vertice)
        print(f"Vizinhos de {vertice}: {', '.join(v) if v else 'nenhum'}")

def exibir_grafo(matriz, vertices):
    print("   ", " ".join(vertices))
    for i, v in enumerate(vertices):
        print(f"{v}  ", " ".join(map(str, matriz[i])))

def main():
    matriz, vertices = criar_grafo()
    while True:
        print("\n--- MENU ---")
        print("1 - Exibir Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos")
        print("7 - Verificar Existência de Aresta")
        print("8 - Calcular Grau dos Vértices")
        print("9 - Verificar Percurso")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(matriz, vertices, v)
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(matriz, vertices, o, d, nd)
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(matriz, vertices, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(matriz, vertices, o, d, nd)
        elif opcao == "6":
            v = input("Vértice: ")
            listar_vizinhos(matriz, vertices, v)
        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", "Sim" if existe_aresta(matriz, vertices, o, d) else "Não")
        elif opcao == "8":
            grau_vertices(matriz, vertices)
        elif opcao == "9":
            caminho = input("Digite o percurso (vértices separados por espaço): ").split()
            print("Percurso válido?", "Sim" if percurso_valido(matriz, vertices, caminho) else "Não")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

def criar_grafo():
    return [], []

def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])
    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])

def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        arestas[:] = [a for a in arestas if vertice not in a]

def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas

def vizinhos(vertices, arestas, vertice):
    return [destino for origem, destino in arestas if origem == vertice]

def grau_vertices(vertices, arestas):
    graus = {}
    for v in vertices:
        entrada = sum(1 for o, d in arestas if d == v)
        saida = sum(1 for o, d in arestas if o == v)
        graus[v] = {"entrada": entrada, "saida": saida, "total": entrada + saida}
    for v, g in graus.items():
        print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")
    return graus

def percurso_valido(arestas, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i + 1]):
            return False
    return True

def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print("Vértice inexistente.")
    else:
        v = vizinhos(vertices, arestas, vertice)
        print(f"Vizinhos de {vertice}: {', '.join(v) if v else 'nenhum'}")

def exibir_grafo(vertices, arestas):
    print(f"Vértices: {vertices}")
    print("Arestas:")
    for origem, destino in arestas:
        print(f"{origem} -> {destino}")

def main():
    vertices, arestas = criar_grafo()
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
            exibir_grafo(vertices, arestas)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(vertices, v)
        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(vertices, arestas, o, d, nd)
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(vertices, arestas, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(arestas, o, d, nd)
        elif opcao == "6":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", "Sim" if existe_aresta(arestas, o, d) else "Não")
        elif opcao == "8":
            grau_vertices(vertices, arestas)
        elif opcao == "9":
            caminho = input("Digite o percurso (vértices separados por espaço): ").split()
            print("Percurso válido?", "Sim" if percurso_valido(arestas, caminho) else "Não")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

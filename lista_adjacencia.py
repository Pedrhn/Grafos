def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    return grafo.get(vertice, [])

def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {', '.join(grafo[vertice]) if grafo[vertice] else 'nenhum'}")
    else:
        print(f"O vértice {vertice} não existe.")

def exibir_grafo(grafo):
    for vertice, adj in grafo.items():
        print(f"{vertice} -> {adj}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)

def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice in grafo:
        for v in grafo:
            if vertice in grafo[v]:
                grafo[v].remove(vertice)
        del grafo[vertice]
    else:
        print(f"O vértice {vertice} não existe.")

def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]

def grau_vertices(grafo):
    graus = {}
    for v in grafo:
        graus[v] = {"saida": len(grafo[v]), "entrada": 0, "total": 0}
    for v in grafo:
        for viz in grafo[v]:
            if viz in graus:
                graus[viz]["entrada"] += 1
    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
    for v, g in graus.items():
        print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")
    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        if not existe_aresta(grafo, caminho[i], caminho[i + 1]):
            return False
    return True

def main():
    grafo = criar_grafo()
    while True:
        print("\n--- MENU ---")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos de um Vértice")
        print("7 - Verificar Existência de Aresta")
        print("8 - Calcular Grau dos Vértices")
        print("9 - Verificar Percurso")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(grafo)
        elif opcao == "2":
            v = input("Nome do vértice: ")
            inserir_vertice(grafo, v)
        elif opcao == "3":
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(grafo, o, d, nd)
        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(grafo, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(grafo, o, d, nd)
        elif opcao == "6":
            v = input("Vértice: ")
            listar_vizinhos(grafo, v)
        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?" , "Sim" if existe_aresta(grafo, o, d) else "Não")
        elif opcao == "8":
            grau_vertices(grafo)
        elif opcao == "9":
            caminho = input("Digite o percurso (vértices separados por espaço): ").split()
            print("Percurso válido?" , "Sim" if percurso_valido(grafo, caminho) else "Não")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

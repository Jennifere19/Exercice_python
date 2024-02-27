A = [
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0]
]


def creat_list_adj(M: list) -> dict:
    # nbre de sommets
    n = len(M)
    # creation de la liste des sommets
    sommets = ["s" + str(i) for i in range(n)]
    list_adj = {}
    for s in sommets:
        list_adj[s] = []
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                list_adj[sommets[i]].append(sommets[j])
    return list_adj


def arret_list(M: list, s_i: int, s_f: int):
    return M[s_i][s_f] == 1


def arret_dic(g: dict, s_i: str, s_f: str):
    return s_f in g.get(s_i)


dico = creat_list_adj(A)
print(arret_dic(dico, "s0", "s1"))
print(arret_list(A, 0, 1))

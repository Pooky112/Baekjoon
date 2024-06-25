import sys

N, M, K = map(int, sys.stdin.readline().split())
def num_of_path(graph):
    for i in range(len(graph) - 1):
        for j in range(1, len(graph[0])):
            graph[i + 1][j] = graph[i][j] + graph[i + 1][j - 1]
    return graph

def find_num_of_path(N, M, K):
    if K == 0:
        graph = [[1 for _ in range(M)] for _ in range(N)]
        print(num_of_path(graph)[-1][-1])
    else:
        k_index = (K//M, K%M-1)
        graph_1 = [[1 for _ in range(k_index[1]+1)] for _ in range(k_index[0]+1)]
        graph_2 = [[1 for _ in range(M - k_index[1])] for _ in range(N - k_index[0])]

        graph_1 = num_of_path(graph_1)
        graph_2 = num_of_path(graph_2)

        print(graph_1[-1][-1] * graph_2[-1][-1])

find_num_of_path(N, M, K)




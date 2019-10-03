"""
    Students template for the first homework of LINMA1691 "Théorie des graphes".

    Authors : Philippe Matthew, Devillez Henri
"""

import itertools
import csv

def check_mapping(A, B, h):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - h an array describing an isomorphism mapping node i from A to node h[i] from B
    Return True if h(A) = B, False otherwise
    """


    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[h[i]][h[j]]:
                return False
    return True


def are_iso(A, B):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions

    Return (Ans, h) with :
        - Ans = True if A and B are isomorphs, False otherwise
        - h an array describing an isomorphim such that h(A) = B
    """

    H = list(itertools.permutations(range(len(A)))) #liste de tous les isomorphes possibles
    for i in range(len(H)):
        if check_mapping(A, B, list(H[i])):
            return True, list(H[i])

    return False, []

def color_ones(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)

    Return an array of same dimension as A containing only ones
    """

    return [1 for _ in range(len(A))]


def color_degree(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)

    Return an array containing the degrees of the nodes of A
    """

    return [sum(A[i]) + A[i][i] for i in range(len(A))]


def color_k_neigh(A, k):
    """
    Input :
        - A an adjacency matrix (array of arrays)
        - k the size of the neighbourhood of the coloring scheme

    Return an array containing the colors as defined in Q4 of the project statement
    The colors have to be structured as a sorted tuple of pairs (k, deg(v))
    """
    degs = color_degree(A)
    neigh = [[(0, degs[i])] for i in range(len(A))]
    B = [[int(i == j) for i in range(len(A))] for j in range(len(A))]
    ispath = [[int(i == j) for i in range(len(A))] for j in range(len(A))]

    for iter in range(1, k+1):
        B = [[sum([a*b for a, b in zip(row, col)]) for col in zip(*B)] for row in A]

        for i in range(len(A)):
            for j in range(len(A)):
                if B[i][j] > 0:
                    ispath[i][j] = 1

                if ispath[i][j] == 1:
                    neigh[i].append((iter, degs[j]))

    for i in range(len(A)):
        neigh[i] = sorted(neigh[i], key=lambda tup: (tup[0], tup[1]))

    return neigh


def are_iso_with_colors(A, B, color = color_ones):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - color a coloring function
    Return (Ans, h) using the coloring heuristic with :
        - Ans = True if A and B are isomorphic, False otherwise
        - h describe an isomorphim such that h(A) = B if Ans = True, h = [] otherwise

    """

    # TO COMPLETE

    return False, []

if __name__ == "__main__":

    # Read Input

    with open('in1.csv', 'r') as fd:
        lines = list(csv.reader(fd, delimiter=','))
        n = int(len(lines)/2)

        A = []
        B = []

        for i in range(n):
            A.append([int(x) for x in lines[i]])

        for j in range(n, 2*n):
            B.append([int(x) for x in lines[j]])

    # Compute answer

    #are_iso, h = are_iso_with_colors(A, B, color_ones)
    #are_iso, h = are_iso_with_colors(A, B, color_degree)
    #are_iso, h = are_iso_with_colors(A, B, lambda x : color_k_neigh(x, 2))

    neigh = color_k_neigh([[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]], 1)
    print(neigh)

    with open('out1.csv', 'r') as fd:
        lines = csv.reader(fd, delimiter=',')
        true_answer = int(next(lines)[0])

        if are_iso != true_answer:
            if true_answer:
                print("Wrong answer: A and B are isomorphic")
            else:
                print("Wrong answer: A and B are not isomorphic")
        else:
            if are_iso:
                if check_mapping(A, B, h):
                    print("Correct answer")
                else:
                    print("Wrong answer: incorrect mapping")




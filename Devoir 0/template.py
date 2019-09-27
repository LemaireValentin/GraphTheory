"""
Template for Homework 0 - LINMA1691

Author : Pierre Veldeman

September 2019
"""

def degMax(A):
    """
    - INPUT : A (list of lists) Adjacency matrix
    - OUTPUT : the biggest degree of the graph represented by A
    
    """
    degmax = 0
    for i in range(len(A)):
        sum = 0
        for j in range(len(A)):
            if i == j:
                sum += 2 * A[i][j]
            else:
                sum += A[i][j]

        if sum > degmax:
            degmax = sum

    return degmax


if __name__ == "__main__":
    A = [[1,1],[1,0]]
    if degMax(A) == 3:
        print("Well done ! :-)")
    else:
        print("Wrong ansmwer :-(")
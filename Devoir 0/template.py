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

    return max([sum(A[i]) + A[i][i] for i in range(len(A))])


if __name__ == "__main__":
    A = [[1,1],[1,0]]
    if degMax(A) == 3:
        print("Well done ! :-)")
    else:
        print("Wrong ansmwer :-(")
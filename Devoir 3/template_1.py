"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math


def spanning_tree_1(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """
    satisfaction = 0

    for i in range(len(roads)):
        satisfaction += roads[i][2]

    sorted_roads = sorted(roads, key=lambda x: x[2])
    node_above = list(range(N))
    size = [1] * N
    edges_in_tree = 0
    i = 0

    def find(i):
        if node_above[i] == i:
            return i
        return find(node_above[i])

    while edges_in_tree < N-1 and i < len(sorted_roads):
        root_0 = find(sorted_roads[i][0])
        root_1 = find(sorted_roads[i][1])
        if size[root_0] > size[root_1]:
            root_0, root_1 = root_1, root_0
        if root_0 != root_1:
            node_above[root_1] = root_0
            size[root_1] += size[root_0]
            edges_in_tree += 1
            satisfaction -= sorted_roads[i][2]
        i += 1
    return satisfaction

    
if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = spanning_tree_1(n, roads)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output)) 
        


"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import math
import random


class Union_Find():
    """
    Disjoint sets data structure for Kruskal's algorithm.
  
    It is useful to keep track of connected components (find(a) == find(b) iff they are connected).  
  
    """
    
    def __init__(self, N):
        """
        INPUT :
            - N : the initial number of disjoints sets
        """
        self.N = N
        self.p = list(range(N))
        self.size = [1]*N
        
    def union(self, a, b, edges_in_tree):
        """
        INPUT :
            - a and b : two elements such that 0 <= a, b <= N-1
        OUTPUT:
            - return nothing
            
        After the operation, the two given sets are merged
        """
        a = self.find(a)
        b = self.find(b)
       
        if a == b:
            return edges_in_tree
       
        # Swap variables if necessary
        if self.size[a] > self.size[b]:
            a, b = b, a
        
        self.size[b] += self.size[a]
        self.p[a] = b
        return edges_in_tree + 1

    def find(self, a):
        """
        INPUT :
            - a : one element such that 0 <= a <= N-1
        OUTPUT:
            - return the root of the element a
        """
        if a != self.p[a]: self.p[a] = self.find(self.p[a])
        return self.p[a]
    

def spanning_tree_2(N, edges):
    # returns binomial expression
    binomial = lambda n, k: fact2(n, k) / math.factorial(n - k)
    # returns n!/k! = (n) * (n-1) * ... * (n-k+1)
    fact2 = lambda n, m: n * fact2(n - 1, m) if n > m else 1
    """ 
    INPUT : 
        - N the number of nodes
        - edges, list of tuples (u, v) giving an edge between u and v

    OUTPUT :
        - return an estimation of the min cut of the graph
        
    self method has to return the correct answer with probability bigger than 0.999
    See project homework for more details
    """
    def karger(nodes, edges):
        """ 
        INPUT : 
            - N the number of nodes
            - edges, list of tuples (u, v) giving an edge between u and v

        OUTPUT :
            - return an estimation of the min cut of the graph
              
        See project homework for more details
        """

        roads = randomize_edges(edges)

        sorted_roads = sorted(roads, key=lambda x: x[2])
        union_find = Union_Find(len(nodes))
        edges_in_tree = 0
        i = 0
        while edges_in_tree < N - 2 and i < len(sorted_roads):
            root_0 = union_find.find(sorted_roads[i][0])
            root_1 = union_find.find(sorted_roads[i][1])
            if union_find.p[root_0] > union_find.p[root_1]:
                root_0, root_1 = root_1, root_0
            if root_0 != root_1:
                union_find.p[root_1] = root_0
                union_find.size[root_1] += union_find.size[root_0]
                edges_in_tree += 1
            i += 1

        cut = 0
        for j in range(len(edges)):
            if union_find.find(sorted_roads[j][0]) != union_find.find(sorted_roads[j][1]):
                cut += 1

        return cut
        
    def randomize_edges(edges):
        """
        INPUT : 
            - edges : a list of undirected edges (u, v) 
        OUTPUT:
            - return a list of random weighted undirected edges (u, v, w)
        """
        
        weighted_edges = [(edges[i][0], edges[i][1], random.randint(0, len(edges))) for i in range(len(edges))]
                
        return weighted_edges 
   
    bin = 1/binomial(N, 2)
    nodes = list(range(N))
    min_cut = karger(nodes, edges)
    probability = bin
    while probability < 0.9999:
        cut = karger(nodes, edges)
        if cut < min_cut:
            min_cut = cut
            probability = bin
        elif cut == min_cut:
            probability += bin

    # TO COMPLETE (apply karger several times)
    # Probability to return the true min cut should be at least 0.9999
    
    return min_cut
    


if __name__ == "__main__":

    # Read Input for the second exercice
    
    with open('in2.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        edges = []
        for edge in range(m):
        
            l = fd.readline().rstrip().split()
            edges.append(tuple([int(x) for x in l]))
            
    # Compute answer for the second exercice
     
    ans = spanning_tree_2(n, edges)
     
    # Check results for the second exercice

    with open('out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output)) 


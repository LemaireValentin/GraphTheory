"""
    Solution for the fourth homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
    
# def matching(T, friends, hiding_places):
def matching(is_reachable):
    """ 
    INPUT : 
        - T, the number of seconds
        - friends, a list of tuples (x, y, v) describing the position (x, y) and velocity v
          of each friend
        - hiding_places, a list of tuple (x, y) giving the position (x, y) of each hiding place
    OUTPUT :
        - return the maximal number of friends that can hide from the game master
        
        See homework statement for more details
    """
    
    ans = 0
    friends = [0] * len(is_reachable)
    hiding_places = [0] * len(is_reachable[0])

    # reachable = lambda T, friend, hiding_place : (friend[0]-hiding_place[0])**2 + (friend[1]-hiding_place[1])**2 <= (T*friend[2])**2 

    accessible_places = [[] for _ in range(len(friends))]

    i = 0
    deleted = 0
    for  i in range(len(friends)):
        for j in range(len(hiding_places)):
            # if reachable(T, friends[i], hiding_places[j]):
            if is_reachable[i][j]:
                accessible_places[i - deleted].append(j)
        if len(accessible_places[i - deleted]) == 0:
            accessible_places.pop(i - deleted)
            deleted += 1

    accessible_places.sort(key=lambda x: len(x))
    
    while len(accessible_places) > 0:
        hp = accessible_places[0].pop()
        accessible_places.pop(0)
        i = 0
        while i < len(accessible_places):
            if hp in accessible_places[i]:
                accessible_places[i].remove(hp)
                if len(accessible_places[i]) == 0:
                    accessible_places.pop(i)
                    i -= 1
            i += 1
        accessible_places.sort(key=lambda x: len(x))
        ans += 1
    return ans

    
if __name__ == "__main__":

    # Read Input
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m, T = int(l[0]), int(l[1]), int(l[2])
        
        friends = []
        for friend in range(n):
            l = fd.readline().rstrip().split()
            friends.append(tuple([float(x) for x in l]))
       
        hiding_places = []
        for hiding_place in range(m):
            l = fd.readline().rstrip().split()
            hiding_places.append(tuple([float(x) for x in l]))

    # Compute answer 
     
    ans = matching(T, friends, hiding_places)
     
    # Check results 

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Test sample : Correct")
        else:
            print("Test sample : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output)) 
        

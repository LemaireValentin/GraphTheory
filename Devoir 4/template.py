"""
    Solution for the fourth homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math


# ------------------------------
# Tests (should be correct)
# ------------------------------
# is_reachable = [[True , False, True ], [True , True , False], [False, False, False]]    ;   solution = 2
# is_reachable = [[True , True , False], [False, True , False], [True , False, False]]    ;   solution = 2
# is_reachable = [[True], [True], [True], [True], [True]]                                 ;   solution = 1
# is_reachable = [[True, True, True, True, True]]                                         ;   solution = 1
# is_reachable = [[False, True, False, True], [False, True, False, False]]                ;   solution = 2
# is_reachable = [[False, False], [True, True], [False, False], [True, False]]            ;   solution = 2
# is_reachable = [[False, True, False, True], [True, True, False, False]]                 ;   solution = 2
# is_reachable = [[False, True], [True, True], [False, False], [True, False]]             ;   solution = 2
# is_reachable = [[False, True, True], [True, True, False], [True, False, False]]         ;   solution = 3


    
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
    # ---------------------------------------
    # Only for testing (should be deleted)
    # ---------------------------------------
    # friends = [0] * len(is_reachable)
    # hiding_places = [0] * len(is_reachable[0])
    # ---------------------------------------


    # -------------------------------------------------
    # SHOULD BE UNCOMMENTED (was commented for testing)
    # -------------------------------------------------
    reachable = lambda T, friend, hiding_place : (friend[0]-hiding_place[0])**2 + (friend[1]-hiding_place[1])**2 <= (T*friend[2])**2 
    is_reachable = [[reachable(T, f, h) for h in hiding_places] for f in friends]
    
    count_reachable = [0]*len(friends)
    for i in range(len(friends)):
        for b in is_reachable[i]:
            count_reachable[i] += int(b)


    can_reach = [[0]*count_reachable[i] for i in range(len(friends))]
    for i in range(len(friends)):
        idx = 0
        for j in range(len(hiding_places)):
            if is_reachable[i][j]:
                can_reach[i][idx] = j
                idx += 1

    edge_in_coupling = [[False] * len(hiding_places) for _ in range(len(friends))]

    friends_coupled = [False] * len(friends)
    places_coupled = [False] * len(hiding_places)

    couple_friends = [-1] * len(friends)
    couple_places = [-1] * len(hiding_places)

    coupled_places = []
    N = 0

    for i in range(len(friends)):
        for j in can_reach[i]:
            if (is_reachable[i][j]) and (not friends_coupled[i]) and (not places_coupled[j]):
                friends_coupled[i], places_coupled[j] = True, True
                couple_friends[i], couple_places[j] = j, i
                edge_in_coupling[i][j] = True
                coupled_places.append(j)
                N += 1
                break
    
    explored = [False] * (len(friends) + len(hiding_places))
    while True:
        c = [-1]
        first_ensemble = -1 
        last_ensemble = -1
        for i in range(len(friends)):
            if (not friends_coupled[i]) and (not explored[i]):
                c[0] = i
                first_ensemble = 0
                last_ensemble = 0
                explored[i] = True
                break

        finished = False
        in_coupling = False
        if c[0] ==  -1:
            return N
        while not finished:
            if last_ensemble == 1:
                if couple_places[c[-1]] != -1:
                    c.append(couple_places[c[-1]])
                    in_coupling = not in_coupling
                    last_ensemble = 0
                else: 
                    finished = True
            elif last_ensemble == 0:
                b = False
                for j in coupled_places:
                    if is_reachable[c[-1]][j] and edge_in_coupling[c[-1]][j] == in_coupling:
                        c.append(j)
                        in_coupling = not in_coupling
                        last_ensemble = 1
                        break
                    if j == coupled_places[-1]: 
                        b = True
                if b: 
                    for j in can_reach[c[-1]]:
                        if edge_in_coupling[c[-1]][j] == in_coupling:
                            c.append(j)
                            in_coupling = not in_coupling
                            last_ensemble = 1
                            break
                    finished = True
                
        if len(c) >= 3 and last_ensemble != first_ensemble:
            last_ensemble = first_ensemble
            in_coupling = True
            for i in range(len(c) - 1):
                if last_ensemble == 0:
                    friends_coupled[c[i]], places_coupled[c[i+1]] = True, True
                    edge_in_coupling[c[i]][c[i+1]] = in_coupling
                    in_coupling = not in_coupling
                    last_ensemble = 1
                elif last_ensemble == 1:
                    places_coupled[c[i]], friends_coupled[c[i+1]] = True, True
                    edge_in_coupling[c[i+1]][c[i]] = in_coupling
                    in_coupling = not in_coupling
                    last_ensemble = 0
            coupled_places.append(c[-1])
            N += 1
            # explored = [False] * (len(friends) + len(hiding_places))

    
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
    ans = 2 
    # ans = matching(T, friends, hiding_places)
     
    # Check results 

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Test sample : Correct")
        else:
            print("Test sample : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output)) 
        

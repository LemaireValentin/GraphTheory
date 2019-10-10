"""
    Students template for the second homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import queue as Q
from collections import deque

# You cannot import other modules
# You do not have to use all imported modules


def shortest_path_1(maze):
    """
    INPUT :
        - maze, a 2D array representing the maze
    OUTPUT :
        - return the minimal number of steps required to go to the exit of the maze.

        See project statement for more details
    """

    # Finds E and S in maze
    def find(maze):
        E = None
        S = None
        for i in range(1,len(maze)-1):
            for j in range(1,len(maze[i])-1):
                if maze[i][j]=="E":
                    E = (i,j)
                if maze[i][j]=="S":
                    S = (i,j)
                if E != None and S != None :
                    return E, S

    E,S = find(maze)

    q = deque()
    tab = [[-42]*len(maze[0]) for _ in range(len(maze))]

    q.append(E)
    tab[E[0]][E[1]] = 0

    while not Q.Empty(q):
        current = q.popleft()
        # North
        if maze[current[0]-1][current[1]] != "#" and tab[current[0]-1][current[1]] < 0 :
            if maze[current[0]-1][current[1]] == "S":
                return tab[current[0]][current[1]] + 1
            q.append((current[0]-1,current[1]))
            tab[current[0]-1][current[1]] = tab[current[0]][current[1]] + 1
        # East
        if maze[current[0]][current[1]+1] != "#" and tab[current[0]][current[1]+1] < 0 :
            if maze[current[0]][current[1]+1] == "S":
                return tab[current[0]][current[1]] + 1
            q.append((current[0],current[1]+1))
            tab[current[0]][current[1]+1] = tab[current[0]][current[1]] + 1
        # South
        if maze[current[0]+1][current[1]] != "#" and tab[current[0]+1][current[1]] < 0 :
            if maze[current[0]+1][current[1]] == "S":
                return tab[current[0]][current[1]] + 1
            q.append((current[0]+1,current[1]))
            tab[current[0]+1][current[1]] = tab[current[0]][current[1]] + 1
        # West
        if maze[current[0]][current[1]-1] != "#" and tab[current[0]][current[1]-1] < 0 :
            if maze[current[0]][current[1]+1] == "S":
                return tab[current[0]][current[1]] + 1
            q.append((current[0],current[1]-1))
            tab[current[0]][current[1]-1] = tab[current[0]][current[1]] + 1
    return -1

def shortest_path_2(tasks, paths):
    """
    INPUT :
        - tasks, the time to achieve each task (in minutes)
        - paths, list of tuples (a, b, t) giving a trail between tasks a and b.
          You need t minutes to walk this trail.
    OUTPUT :
        - return the time you need to finish the game

        See project statement for more details
    """

    return -1


if __name__ == "__main__":

    # Read Input for the first exercice

    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.split(' ')

        n = int(l[0])
        m = int(l[1])

        maze = []
        for row in range(n):
            l = fd.readline().rstrip()
            maze.append(list(l))



    # Compute answer for the first exercice

    ans1 = shortest_path_1(maze)

    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output))

    # Read Input for the second exercice

    with open('in2.txt', 'r') as fd:
        l = fd.readline().split(' ')

        n = int(l[0])
        m = int(l[1])

        tasks = [int(x) for x in fd.readline().rstrip().split(' ')]

        paths = []
        for p in range(n):
            l = fd.readline().rstrip().split(' ')
            paths.append(tuple([int(x) for x in l]))

    # Compute answer for the second exercice

    ans2 = shortest_path_2(tasks, paths)

    # Check results for the second exercice

    with open('out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans2:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans2, expected_output))





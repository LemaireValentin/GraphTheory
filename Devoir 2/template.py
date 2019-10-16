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

    # q = nodes to explore, FIFO
    q = deque()
    # distance from E (-42 if not yet mapped or not attainable)
    dist = [[-42]*len(maze[0]) for _ in range(len(maze))]

    q.append(E)
    dist[E[0]][E[1]] = 0

    while q:
        current = q.popleft()
        # North : checks north path
        # skips if wall or already mapped
        # note : if already mapped, shortest path found because FIFO queue
        if maze[current[0]-1][current[1]] != "#" and dist[current[0]-1][current[1]] < 0 :
            # return if exit found
            if maze[current[0]-1][current[1]] == "S":
                return dist[current[0]][current[1]] + 1
            # add node to list
            q.append((current[0]-1,current[1]))
            # update distance
            dist[current[0]-1][current[1]] = dist[current[0]][current[1]] + 1
        # East : again
        if maze[current[0]][current[1]+1] != "#" and dist[current[0]][current[1]+1] < 0 :
            if maze[current[0]][current[1]+1] == "S":
                return dist[current[0]][current[1]] + 1
            q.append((current[0],current[1]+1))
            dist[current[0]][current[1]+1] = dist[current[0]][current[1]] + 1
        # South : and again
        if maze[current[0]+1][current[1]] != "#" and dist[current[0]+1][current[1]] < 0 :
            if maze[current[0]+1][current[1]] == "S":
                return dist[current[0]][current[1]] + 1
            q.append((current[0]+1,current[1]))
            dist[current[0]+1][current[1]] = dist[current[0]][current[1]] + 1
        # West : once more ?
        if maze[current[0]][current[1]-1] != "#" and dist[current[0]][current[1]-1] < 0 :
            if maze[current[0]][current[1]-1] == "S":
                return dist[current[0]][current[1]] + 1
            q.append((current[0],current[1]-1))
            dist[current[0]][current[1]-1] = dist[current[0]][current[1]] + 1
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
    maxPathLength = 1000 * (len(tasks)+len(paths)) + 1

    passed  = [42] * len(tasks)
    time    = [maxPathLength] * len(tasks)
    time[0] = tasks[0]

    while max(passed) != -1 :
        minValue = maxPathLength
        minIndex = 0
        for i in range(len(passed)) :
            if minValue > time[i] and passed[i] != -1 :
                minIndex = i
                minValue = time[i]
        for i in range(len(paths)) :
            if paths[i][0] == minIndex+1 :
                time[paths[i][1]-1] = min(time[paths[i][1]-1], time[minIndex]+paths[i][2]+tasks[paths[i][1]-1])
            if paths[i][1] == minIndex+1 :
                time[paths[i][0]-1] = min(time[paths[i][0]-1], time[minIndex]+paths[i][2]+tasks[paths[i][0]-1])
        passed[minIndex] = -1

    return time[-1]


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


    print(shortest_path_2([462, 996, 493, 970, 878, 21, 798, 242, 429, 57],  [(3, 1, 631), (7, 2, 177), (4, 3, 661), (7, 4, 532), (8, 5, 317), (7, 6, 852), (8, 7, 77), (5, 9, 842), (2, 10, 256), (1, 4, 978)]))


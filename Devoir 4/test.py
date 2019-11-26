from template import *

# ------------------------------
# Tests (should be correct)
# ------------------------------
# is_reachable = [[0,0,1,0,0,1], [0,0,1,0,1,0], [1,1,0,0,0,0], [0,0,0,0,0,0], [0,1,0,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,0], [0,0,1,0,0,0], [1,1,0,1,1,1], [0,0,1,0,0,0], [0,0,1,0,0,0], [0,0,1,0,0,0]]   ;   solution = 1
# is_reachable = [[0,0,1,0,0,1], [0,0,0,0,0,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,0,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,1], [0,0,0,0,1,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 2
# is_reachable = [[0,0,1,0,0,1], [0,0,0,1,1,0], [1,0,0,0,1,0], [0,1,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]]   ;   solution = 3


def test_1():
    is_reachable = [[0,0,1,0,0,1], [0,0,1,0,1,0], [1,1,0,0,0,0], [0,0,0,0,0,0], [0,1,0,0,0,0], [1,0,0,0,0,0]]
    print('Expected solution %d, output %d' % (2, matching(is_reachable)))

def test_2():
    is_reachable = [[0,0,1,0,0,0], [0,0,1,0,0,0], [1,1,0,1,1,1], [0,0,1,0,0,0], [0,0,1,0,0,0], [0,0,1,0,0,0]]
    print('Expected solution %d, output %d' % (1, matching(is_reachable)))

def test_3():
    is_reachable = [[0,0,1,0,0,1], [0,0,0,0,0,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,0,1,0,0,0], [1,0,0,0,0,0]]
    print('Expected solution %d, output %d' % (2, matching(is_reachable)))

def test_4():
    is_reachable = [[0,0,1,0,0,1], [0,0,0,0,1,0], [1,0,0,0,1,0], [0,0,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]] 
    print('Expected solution %d, output %d' % (2, matching(is_reachable)))

def test_5():
    is_reachable = [[0,0,1,0,0,1], [0,0,0,1,1,0], [1,0,0,0,1,0], [0,1,0,0,0,0], [0,1,1,0,0,0], [1,0,0,0,0,0]] 
    print('Expected solution %d, output %d' % (3, matching(is_reachable)))


test_1()
test_2()
test_3()
test_4()
test_5()

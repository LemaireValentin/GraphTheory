from second_attempt import *

def test_1():
    is_reachable = [[True , False, True ], [True , True , False], [False, False, False]]    ;   solution = 2
    print('TEST 1 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_2():
    is_reachable = [[True , True , False], [False, True , False], [True , False, False]]    ;   solution = 2
    print('TEST 2 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_3():
    is_reachable = [[True], [True], [True], [True], [True]]                                 ;   solution = 1
    print('TEST 3 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_4():
    is_reachable = [[True, True, True, True, True]]                                         ;   solution = 1
    print('TEST 4 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_5():
    is_reachable = [[False, True, False, True], [False, True, False, False]]                ;   solution = 2
    print('TEST 5 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_6():
    is_reachable = [[False, False], [True, True], [False, False], [True, False]]            ;   solution = 2
    print('TEST 6 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_7():
    is_reachable = [[False, True, False, True], [True, True, False, False]]                 ;   solution = 2
    print('TEST 7 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_8():
    is_reachable = [[False, True], [True, True], [False, False], [True, False]]             ;   solution = 2
    print('TEST 8 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_9():
    is_reachable = [[False, True, True], [True, True, False], [True, False, False]]         ;   solution = 3
    print('TEST 9 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_10():
    is_reachable = [[True, False, False], [False, True, False], [False, False, True], [True, True, True]] ;  solution = 3
    print('TEST 10 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_11():
    is_reachable = [[True] * 3 for _ in range(4)]; solution = 3
    print('TEST 11 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_12():
    is_reachable = [[False] * 3 for _ in range(4)]; solution = 0
    print('TEST 12 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_13():
    is_reachable = [[True, False, False, False], [False, True, True, False], [False, False, False, False],[True, False, False, True]] ; solution = 3
    print('TEST 13 : Expected solution %d, output %d' % (solution, matching(is_reachable)))


test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
test_7()
test_8()
test_9()
test_10()
test_11()
test_12()
test_13()

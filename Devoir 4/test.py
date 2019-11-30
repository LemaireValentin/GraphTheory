import numpy as np
from second_attempt import *

def test_01():
    is_reachable = [[True , False, True ], [True , True , False], [False, False, False]]    ;   solution = 2
    print('TEST 01 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_02():
    is_reachable = [[True , True , False], [False, True , False], [True , False, False]]    ;   solution = 2
    print('TEST 02 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_03():
    is_reachable = [[True], [True], [True], [True], [True]]                                 ;   solution = 1
    print('TEST 03 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_04():
    is_reachable = [[True, True, True, True, True]]                                         ;   solution = 1
    print('TEST 04 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_05():
    is_reachable = [[False, True, False, True], [False, True, False, False]]                ;   solution = 2
    print('TEST 05 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_06():
    is_reachable = [[False, False], [True, True], [False, False], [True, False]]            ;   solution = 2
    print('TEST 06 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_07():
    is_reachable = [[False, True, False, True], [True, True, False, False]]                 ;   solution = 2
    print('TEST 07 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_08():
    is_reachable = [[False, True], [True, True], [False, False], [True, False]]             ;   solution = 2
    print('TEST 08 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_09():
    is_reachable = [[False, True, True], [True, True, False], [True, False, False]]         ;   solution = 3
    print('TEST 09 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

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

def test_14():
    is_reachable = [[True, False, False, False], [False, True, False, False], [False, False, True, True],[True, True, False, True]] ; solution = 4
    print('TEST 14 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_15():
    is_reachable = [[True, False, False, False], [False, True, False, False], [False, False, True, True],[True, True, True, True]] ; solution = 4
    print('TEST 15 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_16():
    is_reachable = [[True, False, False, False], [True, False, False, False], [False, False, True, True],[True, True, True, True]] ; solution = 3
    print('TEST 16 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
    
def test_17():
    is_reachable = [[True, True, False, False, True], [True, True, False, False, False], [False, True, True, True, False],[False, False, True, False, False], [False, True, True, False, False]] ; solution = 5
    print('TEST 17 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_18():
    is_reachable = [[True, True, False, False, True], [True, True, False, False, False], [False, True, True, True, False],[False, False, True, False, False]] ; solution = 4
    print('TEST 18 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_19():
    is_reachable = np.array([[True, True, False, False, True], [True, True, False, False, False], [False, True, True, True, False],[False, False, True, False, False]]).T ; solution = 4
    print('TEST 19 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_20():
    is_reachable = [[True, False, True, True, True], [True, True, False, False, False], [True, True, True, False, False],[True, True, True, True, False]] ; solution = 4
    print('TEST 20 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
  
def test_21():
    is_reachable = [[True, False, True, True, True], [True, True, False, False, False], [True, True, True, False, False],[True, True, True, True, False]] ; solution = 4
    print('TEST 21 : Expected solution %d, output %d' % (solution, matching(is_reachable)))

def test_22():
    is_reachable = np.array([[True, False, True, True, True], [True, True, False, False, False], [True, True, True, False, False],[True, True, True, True, False]]).T ; solution = 4
    print('TEST 22 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
  
def test_23():
    is_reachable = [[False, True, True, True, True], [True, True, True, True, False], [False, False, True, False, False], [True, True, True, True, False], [False, True, True, True, True]] ; solution = 5
    print('TEST 23 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
  
def test_24():
    is_reachable = [[False, False], [False, False]] ; solution = 0
    print('TEST 24 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
  
def test_25():
    is_reachable = [[True, True], [False, False]] ; solution = 1
    print('TEST 25 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
    
def test_26():
    is_reachable = np.full((20,4), True) ; solution = 4
    is_reachable[1:,1] = False ; is_reachable[0,3] = False; is_reachable[0,0] = False
    print('TEST 26 : Expected solution %d, output %d' % (solution, matching(is_reachable)))
    

test_01()
test_02()
test_03()
test_04()
test_05()
test_06()
test_07()
test_08()
test_09()
test_10()
test_11()
test_12()
test_13()
test_14()
test_15()
test_16()
test_17()
test_18()
test_19()
test_20()
test_21()
test_22()
test_23()
test_24()
test_25()
test_26()
import code_733_flood_fill as c

def test_example_1():
    s = c.Solution()
    assert s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

def test_example_2():
    s = c.Solution()
    assert s.floodFill([[0,0,0],[0,0,0]], 0, 0, 2) == [[2,2,2],[2,2,2]]

def test_failed():
    s = c.Solution()
    assert s.floodFill([[0,0,0],[0,1,1]],1,1,1) == [[0,0,0],[0,1,1]]

def test_failed_41():
    s = c.Solution()
    assert s.floodFill([[0,0,0],[0,0,0]],0,0,2) == [[2,2,2],[2,2,2]]
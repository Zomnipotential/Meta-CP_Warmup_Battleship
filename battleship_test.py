import pytest
import battleship as bs

def test_getHitProbability(row, column, table, probability):
    assert bs.getHitProbability(row, column, table) == probability

test_getHitProbability(2, 3, [[0, 0, 1],[1, 0, 1]], 0.5)
test_getHitProbability(2, 2, [[1, 1],[1, 1]], 1.0)

from typing import List
# Write any import statements here
import numpy as np

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  return np.sum(G)/(R*C)

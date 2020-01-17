import sys
sys.setrecursionlimit(10000)

def recursion(d):
  try:
    recursion(d + 1)
  except RuntimeError:
    print('재귀 횟수 : {}'.format(d))

recursion(1)

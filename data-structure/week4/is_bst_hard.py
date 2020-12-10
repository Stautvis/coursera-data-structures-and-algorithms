#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if len(tree) == 0:
    return True
  return isBST(tree)

def isBST(node, i = 0, min_number = -sys.maxsize - 1, max_number = sys.maxsize, side = -1):
  if min_number > node[i][0] and max_number == node[i][0] and side == 1:
      return True
  if min_number > node[i][0] or  max_number <= node[i][0]:
      return False

  return ((True if node[i][1] == -1 else isBST(node, node[i][1], min_number, min(max_number, node[i][0]), 0)) and 
          (True if node[i][2] == -1 else isBST(node, node[i][2], max(min_number, node[i][0]),  max_number, 1)))

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

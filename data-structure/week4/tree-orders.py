# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    current_id = 0
    stack = []

    while True:
      if current_id != -1:
        stack.append(current_id)
        current_id = self.left[current_id]
      elif stack:
        current_id = stack.pop()
        yield self.key[current_id]
        current_id = self.right[current_id]
      else:
        break

  def preOrder(self, index = 0):
    if index == 0:
      self.result = []

    self.result.append(self.key[index])

    if self.left[index] != -1:
      self.preOrder(self.left[index])
    if self.right[index] != -1:
      self.preOrder(self.right[index])
  
    if index == 0:
      return self.result

  def postOrder(self,index = 0):
    if index == 0:
      self.result = []

    if self.left[index] != -1:
      self.postOrder(self.left[index])
    if self.right[index] != -1:
      self.postOrder(self.right[index])
    
    self.result.append(self.key[index])
  
    if index == 0:
      return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

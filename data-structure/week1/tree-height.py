# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

	def compute_height(self):
		return self.calculate(self.parent)

	def calculate(self, nodes, index = -1):
		if index == -1:
			try: return self.calculate(nodes, nodes.index(index))
			except ValueError: return 0

		branches_count = nodes.count(index)
		if branches_count == 0: return 1 #if no more branches

		branches = []
		begining = 0
		for i in range(branches_count):
			new_index = nodes.index(index, begining)
			branches.append(1 + self.calculate(nodes, new_index))
			begining = new_index + 1
		return max(branches)



def main():
	tree = TreeHeight()
	tree.read()
	print(tree.compute_height())

threading.Thread(target=main).start()

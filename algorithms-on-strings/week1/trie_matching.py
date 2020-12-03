# python3
import sys

class Node:
	def __init__ (self):
		self.next = {
			'A': -1,
			'C': -1,
			'G': -1,
			'T': -1,
		}
	def is_leaf(self):
		for node in self.next.values():
			if node != -1:
				return False
		return True

def build_trie(patterns):
	trie = Node()
	for pattern in patterns:
		current_node = trie
		for letter in pattern:
			if current_node.next[letter] == -1:
				current_node.next[letter] = Node()
			current_node = current_node.next[letter]
	return trie
def solve (text, n, patterns):
	result = []
	n = 0
	trie = build_trie(patterns)

	while n < len(text):
		if prefix_trie_matching(text[n:], trie):
			result.append(n)
		n += 1

	return result
def prefix_trie_matching(text, trie):
	n = 0

	letter = text[n]
	current_node = trie

	while True:
		if current_node.is_leaf():
				return True	
		elif current_node.next[letter] != -1:
			current_node = current_node.next[letter]
			if n < len(text) - 1:
				letter = text[n + 1]
				n += 1
			else:
				return current_node.is_leaf()
		else:
			return False

if __name__ == "__main__":
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]

	ans = solve(text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
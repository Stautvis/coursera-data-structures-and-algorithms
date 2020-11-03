# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    
    stack = []
    for i, char in enumerate(text):
        if char not in "(){}[]": continue # if not required char - move next
        if char in "})]" and len(stack) == 0: return i + 1 # if no opening tag, but found closing - return index
        if char in "([{":
            stack.append(Bracket(char, i))
            continue

        if len(stack) == 0: return i + 1
        top = stack.pop()

        if  ((top.char == "[" and char != "]") or
            (top.char == "(" and char != ")") or
            (top.char == "{" and char != "}")):
            return i + 1
    return "Success" if len(stack) == 0 else stack.pop().position + 1




def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

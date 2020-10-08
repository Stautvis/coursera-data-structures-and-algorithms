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
            stack.append(char)
            continue

        if len(stack) == 0: return i + 1
        top = stack.pop()

        if  ((top == "[" and char != "]") or
            (top == "(" and char != ")") or
            (top == "{" and char != "}")):
            return i + 1
    return "Success" if len(stack) == 0 else len(text)




def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randrange(1, len(pattern) - 1)
    result = []
    pattern_hashed = poly_hash(pattern, p, x)
    h = precompute_hashes(text, pattern, p, x)

    for index in range(len(text) - len(pattern)):
        if pattern_hashed != h[index]:
            continue
        if text[index:index + len(pattern)] == pattern:
            result.append(index)
    return result

def precompute_hashes(text, pattern, primer, multiplier):
    text_range = len(text) - len(pattern)
    h = [None for _ in range(text_range + 1)]
    string = text[text_range:len(text) - 1]
    h[text_range] = hash(string)
    y = 1
    for index in range(1,len(pattern)):
        y = (y * multiplier) % primer
    for index in range(text_range - 1, 0, -1):
        h[index] = (multiplier * h[index + 1] + ord(text[index]) - y * ord(text[index + len(pattern)])) % primer
    return h


def poly_hash(string, prime, multiplier):
    hashed = 0
    for c in reversed(string):
        hashed = (hashed * multiplier + ord(c)) % prime
    return hashed

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


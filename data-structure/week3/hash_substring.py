# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    result = []
    pattern_hashed = poly_hash(pattern, p, x)
    h = precompute_hashes(text, pattern, p, x)

    for index in range(len(text) - len(pattern) + 1):
        if pattern_hashed != h[index]:
            continue
        if text[index:index + len(pattern)] == pattern:
            result.append(index)
    return result

def precompute_hashes(text, pattern, primer, multiplier):
    text_range = len(text) - len(pattern)
    h = [0] * (text_range + 1)
    string = text[-len(pattern):]
    h[text_range] = poly_hash(string, primer, multiplier)
    y = 1
    for index in range(1,len(pattern) + 1):
        y = (y * multiplier) % primer
    for index in reversed(range(text_range)):
        hash_ = (multiplier * h[index + 1] + ord(text[index]) - y * ord(text[index + len(pattern)]))
        while hash_ < 0:
            hash_ += primer
        h[index] = hash_ % primer
    return h


def poly_hash(string, prime, multiplier):
    hashed = 0
    for c in reversed(string):
        hashed = (hashed * multiplier + ord(c)) % prime
    return hashed

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

